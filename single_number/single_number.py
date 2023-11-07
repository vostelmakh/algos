from collections import defaultdict
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_dict = defaultdict(int)

        for num in nums:
            nums_dict[num] += 1

        for key in nums_dict:
            if nums_dict[key] == 1:
                return key

        return 0

    def singleNumberXoR(self, nums: List[int]) -> int:
        answer = 0

        for num in nums:
            answer ^= num

        return answer
