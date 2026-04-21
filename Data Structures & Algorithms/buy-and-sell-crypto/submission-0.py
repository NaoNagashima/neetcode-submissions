class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = float('inf')
        min_index = -1
        profit = 0

        for i in range(len(prices)):
            if prices[i] < min_buy:
                min_buy = prices[i]
                min_index = i
            else:
                if min_buy != float('inf') and prices[i] - min_buy > profit:
                    profit = prices[i] - min_buy
        
        return profit

            