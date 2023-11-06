def getX2arr(arr):
    max_negative_num_idx = None

    for i in range(len(arr)):
        if arr[i] < 0 and (max_negative_num_idx is None or arr[i] > arr[max_negative_num_idx]):
            max_negative_num_idx = i

    res = []

    if max_negative_num_idx == None:
        # все числа положительные, возводим их в квадрат
        for num in arr:
            res.append(num * num)

        return res

    if (max_negative_num_idx == len(arr) - 1):
        # все числа отрицательные, возводим их в квадрат
        for num in reversed(arr):
            res.append(num * num)

        return res

    left = max_negative_num_idx
    right = max_negative_num_idx + 1

    while len(res) < len(arr):
        if right > len(arr) - 1:
            res.append(arr[left] * arr[left])
            left -= 1
            continue

        if left < 0:
            res.append(arr[right] * arr[right])
            right += 1
            continue

        if abs(arr[left]) > arr[right]:
            res.append(arr[right] * arr[right])
            right += 1
        else:
            res.append(arr[left] * arr[left])
            left -= 1

    return res

def test_getX2arr():
    arr = [1, 2, 3, 4]
    expected = [1, 4, 9, 16]
    result = getX2arr(arr)
    assert result == expected, f"Expected {expected}, but got {result}"

    arr = [-4, -3, -2, -1]
    expected = [1, 4, 9, 16]
    result = getX2arr(arr)
    assert result == expected, f"Expected {expected}, but got {result}"

    arr = [-2, -1, 0, 4]
    expected = [0, 1, 4, 16]
    result = getX2arr(arr)
    assert result == expected, f"Expected {expected}, but got {result}"

    arr = []
    expected = []
    result = getX2arr(arr)
    assert result == expected, f"Expected {expected}, but got {result}"

    arr = [-5]
    expected = [25]
    result = getX2arr(arr)
    assert result == expected, f"Expected {expected}, but got {result}"

    arr = [5]
    expected = [25]
    result = getX2arr(arr)
    assert result == expected, f"Expected {expected}, but got {result}"

    print("All tests passed")

test_getX2arr()
