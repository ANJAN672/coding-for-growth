class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        consumed=0
        while numBottles>=numExchange:
            consumed+=numExchange
            numBottles-=numExchange
            numBottles+=1
        return numBottles+consumed