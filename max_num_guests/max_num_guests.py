# Даны даты заезда и отъезда каждого гостя. 
# Для каждого гостя дата заезда строго раньше даты отъезда (то есть каждый гость останавливается хотя бы на одну ночь). 
# В пределах одного дня считается, что сначала старые гости выезжают, а затем въезжают новые. 
# Найти максимальное число постояльцев, которые одновременно проживали в гостинице (считаем, что измерение количества постояльцев происходит в конце дня).

# sample = [ (1, 2), (1, 3), (2, 4), (2, 3), ]

from typing import List

def max_num_guests_n2(guests: List[tuple]) -> int:
    guests_at_day = {}

    for guest in guests:
        for day in range(guest[0], guest[1]):
            if day in guests_at_day:
                guests_at_day[day] += 1
            else:
                guests_at_day[day] = 1

    max_guests = 0

    for guests in guests_at_day:
        max_guests = max(max_guests, guests) 
    
    return max_guests

def max_num_guests_nlogn(guests: List[tuple]) -> int:
    max_guests = 0

    arriving = {}
    leaving = {}

    for guest in guests:
        arriving_day = guest[0]

        if arriving_day in arriving:
            arriving[arriving_day] += 1
        else:
            arriving[arriving_day] = 1

        leaving_day = guest[1]

        if leaving_day in leaving:
            leaving[leaving_day] += 1
        else:
            leaving[leaving_day] = 1

    current_guests = 0

    for day in sorted(set(arriving.keys()) | set(leaving.keys())):
        if day in arriving:
            current_guests += arriving[day]

        if day in leaving:
            current_guests -= leaving[day]

        if current_guests > max_guests:
            max_guests = current_guests

    return max_guests

res = max_num_guests_n2([ (1, 2), (1, 3), (2, 4), (2, 3), ])

print(res)