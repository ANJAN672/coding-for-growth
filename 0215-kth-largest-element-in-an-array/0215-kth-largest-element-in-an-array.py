import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i]*=-1
        heapq.heapify(nums)
        # print(nums)
        while k!=0:
            res=-heapq.heappop(nums)
            k-=1
        return res
