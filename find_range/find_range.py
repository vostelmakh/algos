# Дан список интов nums и число-цель target.
# Нужно найти такой range, чтобы сумма его элементов давала число-цель.

def find_range_with_target_sum(nums, target):
    left = 0
    right = 0

    current_sum = 0

    while left <= right:
        if current_sum == target:
            return [left, right]

        if current_sum < target:
            current_sum += nums[right]

            right += 1
        else:
            current_sum -= nums[left]

            left += 1

    return None
