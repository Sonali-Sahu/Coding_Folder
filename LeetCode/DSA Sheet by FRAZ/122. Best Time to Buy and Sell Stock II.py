https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

# TC =  O(n)
# SC = O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price = prices[i]
            else:
                max_profit += prices[i]-min_price
                min_price = prices[i]
        return max_profit
