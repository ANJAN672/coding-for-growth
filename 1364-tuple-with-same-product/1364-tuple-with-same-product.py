from collections import Counter
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prod=Counter()
        res=0
        j=len(nums)-1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                p=nums[i]*nums[j]
                prod[p]+=1
        for count in prod.values():
            if count>=2:
                res+=count*(count-1)//2
        return res*8
        