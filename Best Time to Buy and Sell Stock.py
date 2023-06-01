# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]
        max_profit = 0
        for i in prices:
            if min_price>i:
                min_price = i
            else:
                profit = i - min_price
            max_profit = max(max_profit,profit)

        return max_profit
            
