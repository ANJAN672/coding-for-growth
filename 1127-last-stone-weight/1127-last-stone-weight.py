import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==0:
            return 0
        if len(stones)==1:
            return stones[0]
        for i in range(len(stones)):
            stones[i]=-stones[i]
        heapq.heapify(stones)
        while len(stones)>1:
            x=-heapq.heappop(stones)
            y=-heapq.heappop(stones)
            if x!=y:
                res=abs(x-y)
                heapq.heappush(stones,-res)
            if x==y:
                continue
        return -stones[0] if stones else 0

