class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if len(nums)<2:
            return 0
        heapq.heapify(nums)
        op=0
        j=0
        for i in range(len(nums)-1):
            if nums[j]>=k:
                break
            x=heapq.heappop(nums)
            y=heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))
            op+=1
        return op