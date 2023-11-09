def calculate(arr):
    n = len(arr)
    if n < 2:
        raise ValueError("arr must contain at least 2 elements")

    min1 = float('inf')
    min2 = float('inf')
    max1 = float('-inf')
    max2 = float('-inf')

    for i in range(n):
        if arr[i] <= min1:
            min2 = min1
            min1 = arr[i]
        elif arr[i] < min2:
            min2 = arr[i]

        if arr[i] >= max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2:
            max2 = arr[i]

    if min1 > 0:
        return min1 * min2
    elif max1 < 0:
        return max1 * max2
    else:
        return min1 * max1
