# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_profit = 0
        current_min = prices[0]

        for i in range(1, len(prices)):
            price = prices[i]

            max_profit = max(max_profit, price - current_min)

            current_min = min(current_min, price)

        return max_profit
