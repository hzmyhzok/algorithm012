class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            if i > 0:
                tmp = prices[i] - prices[i-1]
                if tmp >= 0:
                    profit += tmp
        return profit