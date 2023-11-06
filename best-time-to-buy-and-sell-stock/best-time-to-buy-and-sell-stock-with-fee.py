# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
# You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.
# Find the maximum profit you can achieve.

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0

        buy = float('-inf')
        sell = 0

        for price in prices:
            next_buy = max(buy, sell - (price + fee))
            next_sell = max(sell, buy + price)

            sell = next_sell
            buy = next_buy

        return sell
