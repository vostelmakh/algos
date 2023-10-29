# Перенести нули в конец массива, сохранив порядок остальных элементов

# [1,0,8,9] → [1,8,9,0]

def move_zeros(nums):
    right, left = 0, 0

    while right < len(nums):
        if nums[left] == 0 and nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]

        if nums[left] != 0:
            left += 1
           
        right += 1

    return nums


print(move_zeros([0,0,8,9]))
