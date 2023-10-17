from math import log2

# x * log2(x) = Y. Find value of Y
def solve_equation(value):
    left, right = 1, value

    for _ in range(100):
        mid = (left + right) / 2

        result = mid * log2(mid)

        if result == value:
            return mid

        if result > value:
            right = mid
        else:
            left = right

    return None