from typing import List

class Solution:
    result = []

    def backtrack(self, current, nums):
        if current == len(nums):
            self.result.append(nums[:])        
            return
        
        for i in range(current, len(nums)):

            nums[i], nums[current] = nums[current], nums[i]
            
            self.backtrack(current + 1, nums)

            nums[i], nums[current] = nums[current], nums[i]


    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.backtrack(0, nums)
        return self.result
    
solution = Solution()

print(solution.permute([1,2]))

# backtrack(0, [1, 2, 3])
# ├── backtrack(1, [1, 2, 3])
# │   ├── backtrack(2, [1, 2, 3])
# │   │   └── backtrack(3, [1, 2, 3])
# │   ├── backtrack(2, [1, 3, 2])
# │   │   └── backtrack(3, [1, 3, 2])
# │   └── backtrack(2, [1, 3, 2])
# │       └── backtrack(3, [1, 3, 2])
# ├── backtrack(1, [2, 1, 3])
# │   ├── backtrack(2, [2, 1, 3])
# │   │   └── backtrack(3, [2, 1, 3])
# │   ├── backtrack(2, [2, 3, 1])
# │   │   └── backtrack(3, [2, 3, 1])
# │   └── backtrack(2, [2, 3, 1])
# │       └── backtrack(3, [2, 3, 1])
# └── backtrack(1, [3, 2, 1])
#     ├── backtrack(2, [3, 2, 1])
#     │   └── backtrack(3, [3, 2, 1])
#     ├── backtrack(2, [3, 1, 2])
#     │   └── backtrack(3, [3, 1, 2])
#     └── backtrack(2, [3, 1, 2])
#         └── backtrack(3, [3, 1, 2])