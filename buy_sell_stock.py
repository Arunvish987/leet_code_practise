class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pro = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                profit = prices[j]
                profit1 = prices[i]
                pro = profit - profit1
                if pro > max_pro:
                    max_pro = pro
        return max_pro
