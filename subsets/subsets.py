# Given an integer array nums of unique elements, return all possible subsets
# The solution set must not contain duplicate subsets. Return the solution in any order.

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            new_subsets = []
            
            for subset in result:
                new_subsets.append(subset + [num])

            result += new_subsets

        return result
    

nums = [1,2,3]

sol = Solution()

print(sol.subsets(nums), len(sol.subsets(nums)))