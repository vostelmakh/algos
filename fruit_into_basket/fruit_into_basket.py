from collections import defaultdict
from typing import List


class Solution:
    def total_fruit(self, fruits: List[int]) -> int:
        max_fruits = 2

        left, right = 0, 0

        fruits_dict = defaultdict(int)

        result = 0

        while right < len(fruits):
            right_fruit = fruits[right]
            fruits_dict[right_fruit] += 1

            while len(fruits_dict) > max_fruits:
                left_fruit = fruits[left]

                fruits_dict[left_fruit] -= 1

                if fruits_dict[left_fruit] == 0:
                    del fruits_dict[left_fruit]

                left += 1

            result = max(result, right - left + 1)

            right += 1

        return result
