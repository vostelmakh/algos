# Дан список интов, повторяющихся элементов в списке нет.
# Нужно преобразовать это множество в строку, сворачивая соседние по числовому ряду числа в диапазоны.
# Примеры:
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"

def arr2interval(numbers):
    groups = []

    sorted_nums = sorted(numbers)

    num_group = []

    for num in sorted_nums:
        if len(num_group) == 0:
            num_group.append(num)
            continue

        if num == num_group[-1] + 1:
            num_group.append(num)
            continue

        groups.append(num_group)

        num_group = [num]

    if len(num_group) > 0:
        groups.append(num_group)

    result = ''

    for group in groups:
        if len(result) > 0:
            result += ','

        first = group[0]
        last = group[-1]

        if first == last:
            result += str(first)
        else:
            result += str(first) + "-" + str(last)

    return result
