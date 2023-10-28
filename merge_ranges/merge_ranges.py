# Слияние отрезков:

# Вход: [1, 3] [2, 4] [100, 200] [2, 4]
# Выход: [1, 4] [100, 200]

from typing import List, Tuple


def merge(ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    if not ranges:
        return []
    
    result_ranges = []
    last_range = None

    for range in sorted(ranges):
        if not last_range:
            last_range = range
            continue

        if range[0] <= last_range[1]:
            last_range = (last_range[0], max(last_range[1], range[1]))
        else:
            result_ranges.append(last_range)
            last_range = range
    else:
        result_ranges.append(last_range)

    return result_ranges

res = merge([(1, 3), (100, 200), (2, 4)] )
print(res)