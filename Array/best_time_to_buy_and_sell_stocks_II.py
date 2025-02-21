class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]            

        for price in prices:
            if price < min_price:
                min_price = price
            
            current_profit = price - min_price

            if current_profit > 0:
                max_profit += current_profit
                current_profit = 0
                min_price = price

        return max_profit
