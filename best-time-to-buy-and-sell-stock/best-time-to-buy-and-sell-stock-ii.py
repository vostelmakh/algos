# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        buy = float('-inf')
        sell = 0

        for price in prices:
            print('price:', price, "sell:", sell, "buy:", buy)

            next_buy = max(buy, sell - price)
            next_sell = max(sell, buy + price)

            print("next_buy:", next_buy, "next_sell:", next_sell)

            sell = next_sell
            buy = next_buy

        return sell

    def slidingWindow(self, prices):
        left = 0
        right = 1

        totalProfit = 0

        while right < len(prices):
            currentPrice = prices[right]
            prevPrice = prices[left]

            if (currentPrice <= prevPrice):
                left = right
                right += 1
                continue

            while (right + 1 < len(prices) and prices[right + 1] > prices[right]):
                right += 1

            totalProfit += prices[right] - prices[left]

            if (right + 1 < len(prices)):
                left = right + 1
                right += 1

        return totalProfit


sol = Solution()
# res = sol.maxProfit([7,1,5,3,6,4])
# print(res)
res = sol.slidingWindow([7, 1, 5, 3, 6, 4])
print(res)
