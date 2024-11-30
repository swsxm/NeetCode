from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = None

        for price in prices:
            if min_price is None:
                min_price = price
                continue

            if price < min_price:
                min_price = price

            max_profit = max(max_profit, price - min_price)

        return max_profit
