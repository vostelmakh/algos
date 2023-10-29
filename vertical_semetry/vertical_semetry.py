# Дан массив точек с целочисленными координатами (x, y).
# Определить, существует ли вертикальная прямая, делящая точки на 2 симметричных относительно этой прямой множества.
# Note: Для удобства точку можно представлять не как массив [x, y], а как объект {x, y}

from ctypes.wintypes import POINT
from statistics import mean
from typing import List


def is_vertical_symmetry(points: List[POINT]) -> bool:
    # сначала найдём вертикальную прямую в середине всех точек
    x_center = mean(p.x for p in points)

    unmatched_points = {}

    for point in points:
        if point.x == x_center:
            continue

        brother = str(x_center * 2 - point.x) + ';' + str(point.y)

        if brother in unmatched_points:
            unmatched_points[brother] -= 1
        else:
            point_str = str(point.x) + ';' + str(point.y)
            unmatched_points[point_str] = 1

    for val in unmatched_points.values():
        if val > 0:
            return False

    return True

print(
    is_vertical_symmetry([
        POINT(1, 1), 
        POINT(1, 2),
        POINT(2, 2),
        POINT(2, 1),
        POINT(3, 2),
        POINT(2, 1),
        ]
    ))