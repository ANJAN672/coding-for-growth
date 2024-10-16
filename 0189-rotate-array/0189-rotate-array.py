class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # In case k is greater than the size of the array
        nums[:] = nums[-k:] + nums[:-k]  # Slice the array and concatenate
        return nums  # This return statement isn't necessary as the problem states      in-place modification
