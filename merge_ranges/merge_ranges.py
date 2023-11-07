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


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    res = []
    last_range = None

    for interval in intervals:
        if not last_range:
            last_range = interval
            continue

        if last_range[1] > newInterval[0]:
            last_range = [
                last_range[0],
                max(last_range[1], newInterval[1])
            ]

            if last_range[1] > interval[0]:
                last_range = [
                    last_range[0],
                    max(last_range[1], interval[1])
                ]
            else:
                res.append(last_range)
                last_range = interval
        else:
            res.append(last_range)
            last_range = interval

    if last_range:
        res.append(last_range)

    return res


# res = merge([(1, 3), (100, 200), (2, 4)] )
res = insert([[1,5]], [2, 7])
print(res)
