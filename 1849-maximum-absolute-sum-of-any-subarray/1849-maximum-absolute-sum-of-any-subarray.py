class Solution:
    def maxAbsoluteSum(self, nums):
        summ, minSum, maxSum = 0, 0, 0
        for num in nums:
            summ += num
            maxSum = max(maxSum, summ)
            minSum = min(minSum, summ)
        return abs(maxSum - minSum)