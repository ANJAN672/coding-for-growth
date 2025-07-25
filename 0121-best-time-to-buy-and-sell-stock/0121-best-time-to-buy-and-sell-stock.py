class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minm=prices[0]
        max_profit=0
        for i in prices:
            if i < minm:
                minm = i
            else:
                profit=i-minm
                max_profit=max(profit,max_profit)
        return max_profit