# Дан отсортированный массив чисел - arr, индекс элемента index и целое число k.
# Необходимо вернуть в любом порядке k чисел из массива, которые являются ближайшими по значению к элементу а[index].
from typing import List


def find_k_neares(arr, idx, k):
    if k > len(arr):
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


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k >= len(arr):
            return arr

        left = 0
        right = len(arr) - 1

        while right - left + 1 > k:
            diff_left = abs(x - arr[left])
            diff_right = abs(x - arr[right])

            if diff_left > diff_right:
                left += 1
            else:
                right -= 1

        return arr[left:right+1]


solution = Solution()

print(solution.findClosestElements([1, 2, 3, 4, 5], 4, 3))
print(solution.findClosestElements([1], 1, 1))
