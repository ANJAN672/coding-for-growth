from collections import defaultdict
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1=defaultdict(int)
        for i in nums:
            dict1[i]+=1
        return max(dict1, key=dict1.get)