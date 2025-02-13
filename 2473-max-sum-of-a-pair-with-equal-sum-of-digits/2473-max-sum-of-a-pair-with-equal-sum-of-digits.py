class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        max_arr=[0]*82
        ans=-1
        for x in nums:
            sumi=sum(map(int,str(x)))
            if max_arr[sumi] !=0:
                ans=max(ans,x+max_arr[sumi])
            max_arr[sumi]=max(max_arr[sumi],x)
        return ans