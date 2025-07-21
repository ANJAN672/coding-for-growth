class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count=len(nums)
        for _ in range(len(nums)):
            if val in nums:
                nums.remove(val)
                count -= 1
        return count