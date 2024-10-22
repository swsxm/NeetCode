from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            print(l, r)
            if prices[l] < prices[r]:
                price = prices[r] - prices[l]
                max_profit = max(price, max_profit)
                r += 1
            else:
                l = r
                r += 1
        return max_profit

    def maxProfit2(self, prices: List[int]) -> int:
        max_profit = 0
        low = prices[0]

        for price in prices:
            if price < low:
                low = price
            max_profit = max(price-low, max_profit)
        return max_profit
            

Test = Solution()
print(Test.maxProfit2([10,8,7,5,2]))
