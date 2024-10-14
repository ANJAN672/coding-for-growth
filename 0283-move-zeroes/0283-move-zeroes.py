class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0  # Pointer to track the position of the next non-zero element

        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap non-zero element nums[i] with nums[j]
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return nums
