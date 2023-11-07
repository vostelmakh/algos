# https://leetcode.com/problems/maximum-subarray/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            cur_sum = max(num, cur_sum + num)
            max_sum = max(cur_sum, max_sum)

        return max_sum


solution = Solution()

print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
