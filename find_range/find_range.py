# Дан список интов и число-цель. 
# Нужно найти такой range, чтобы сумма его элементов давала число-цель.

def find_range_with_target_sum(nums, target):
    left = 0
    right = 0

    sum = 0

    while left <= right:
        if sum == target:
            return range(left, right)
        
        if sum < target:
            sum += nums[right]

            right += 1
        else:
            sum -= nums[left]

            left += 1

    return None
        
nums = [1, 2, 4, 4, 3, 2, 1]
target = 9

result = find_range_with_target_sum(nums, target)
if result is not None:
    print(f"Диапазон с требуемой суммой: {result}")
else:
    print("Диапазон с требуемой суммой не найден")