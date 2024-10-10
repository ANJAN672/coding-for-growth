class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        indicies = sorted(range(N), key=lambda x: nums[x])
        ans = 0
        cur_min = indicies[0]
        for i in range(1, N):
            ans = max(ans, indicies[i] - cur_min)
            cur_min = min(cur_min, indicies[i])
        return ans