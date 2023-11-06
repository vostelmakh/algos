# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        buy = float('-inf')
        sell = 0
        cooldown = 0

        for price in prices:
            next_buy = max(buy, cooldown - price)
            next_sell = buy + price

            cooldown = max(sell, cooldown)

            sell = next_sell
            buy = next_buy

        return max(sell, cooldown)
