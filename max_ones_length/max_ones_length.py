# Дан массив из нулей и единиц. Нужно определить, какой максимальный по длине подинтервал единиц можно получить, удалив ровно один элемент массива.

# [1, 1, 0]

def max_ones_length(seq):
    groups = []

    count = 0

    for num in seq:
        if num == 0:
            if count == 0:
                groups.append(0)
            else:
                groups.append(count)
                groups.append(0)
            
            
            count = 0
        else:
            count += 1

    return groups