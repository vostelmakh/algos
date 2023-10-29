def bin_search(arr, target):
    left_idx = 0
    right_idx = len(arr) - 1

    while left_idx < right_idx:
        mid_idx = int(((left_idx + right_idx) / 2))

        if (target == arr[mid_idx]):
            return mid_idx

        if (target > arr[mid_idx]):
            left_idx = mid_idx
        else: 
            right_idx = mid_idx

    return None

    