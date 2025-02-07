class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res,sol=[],[]
        def backtrack(i):
            
            if len(sol)==len(nums):
                res.append(sol[:])
                return

            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack(i+1)
                    sol.pop()
        backtrack(0)
        return res