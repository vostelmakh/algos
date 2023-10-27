# Дан массив из нулей и единиц. Нужно определить, какой максимальный по длине подинтервал единиц можно получить, удалив ровно один элемент массива.

def max_ones_length(seq):
    groups = []

    count = 0

    for num in seq:
        if num == 0:
            if count == 0:
                groups.append(0)
            else:
                groups.append(count)
            
            count = 0
        else:
            count += 1

    if (count > 0):
        groups.append(count)

    if (len(groups) == 0):
        return 0 

    max_seq = groups[0]

    max_index = len(groups) - 1

    for index in range(len(groups) - 1):
        prevIndex = index - 1
        nextIndex = index + 1

        if (prevIndex > 0):
            val = groups[prevIndex] + groups[index]
            max_seq = max(val, max_seq)
        
        if (nextIndex <= max_index):
            val = groups[nextIndex] + groups[index]
            max_seq = max(val, max_seq)

        if (prevIndex > 0 and nextIndex <= max_index):
            val = groups[nextIndex] + groups[prevIndex]
            max_seq = max(val, max_seq)

    return max_seq