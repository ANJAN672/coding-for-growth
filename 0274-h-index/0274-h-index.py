class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n=len(citations)
        arr1=[0]*(n+1)
        for c in citations:
            arr1[min(c,n)]+=1
        h=n
        papers=arr1[n]
        while papers < h:
            h-=1
            papers+=arr1[h]
        return h

        # print(arr1)