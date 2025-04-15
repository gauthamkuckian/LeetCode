class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min :
                min = prices[i]
            else:
                if (prices[i] - min) > max_profit:
                    max_profit =  (prices[i] - min)
        return max_profit

