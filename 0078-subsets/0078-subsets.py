class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res,sol=[],[]

        def backtrack(i):
            if i==len(nums):
                res.append(sol[:])
                return
            #dont pick
            backtrack(i+1)
            #have to pick
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        backtrack(0)
        return res