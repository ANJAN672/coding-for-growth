class Solution(object):
    def singleNumber(self, nums):
        uniqNum = 0
        for idx in nums:
            uniqNum ^= idx
        return uniqNum