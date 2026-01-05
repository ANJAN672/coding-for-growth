class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest=prices[0]
        total=0
        for i in range(1,len(prices)):
            if prices[i]<lowest:
                lowest=prices[i]
            total+=prices[i]-lowest
            lowest=prices[i]
        return total