# https://leetcode.com/problems/monotonic-array/

# An array is monotonic if it is either monotone increasing or monotone decreasing.
#
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.
from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True

        is_increasing = True
        is_decreasing = True

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                is_increasing = False

            if nums[i - 1] < nums[i]:
                is_decreasing = False

        return is_increasing or is_decreasing
