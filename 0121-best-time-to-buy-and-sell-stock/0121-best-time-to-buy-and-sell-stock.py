class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest=prices[0]
        best_profit=0
        for i in range(len(prices)):
            if lowest > prices[i]:
                lowest=prices[i]
            best_profit= max(best_profit,prices[i]-lowest)
        return best_profit