# Дан отсортированный массив чисел а, индекс элемента index и целое число k. Необходимо вернуть в любом порядке k чисел из массива, которые являются ближайшими по значению к элементу а[index].

# find_k_closest([2,3,5,7,11], index=3, k=2) -> {5,7}

# find_k_closest([4,12,15,15,24], index=1, k=3) -> {12,15,15}

# find_k_closest([2,3,5,7,11], index=2, k=2) -> {5,7} или {3,5}

def find_k_neares(arr, idx, k):
    if (k > len(arr)):
        return []

    central_elem = arr[idx]
    left = idx - 1
    right = idx + 1

    result = [central_elem]

    while len(result) < k:
        if left >= 0 and right < len(arr):
            diff_left = abs(central_elem - arr[left])
            diff_right = abs(central_elem - arr[right])

            if diff_left <= diff_right:
                result.append(arr[left])
                left -= 1
            else:
                result.append(arr[right])
                right += 1
        elif left >= 0:
            result.append(arr[left])
            left -= 1
        elif right < len(arr):
            result.append(arr[right])
            right += 1

    return result

print(find_k_neares([4,12,15,15,24], 1, 3))