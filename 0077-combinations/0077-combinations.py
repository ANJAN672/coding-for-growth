class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res,sol=[],[]
        def backtrack(i):
            if len(sol)==k:
                res.append(sol[:])
                return
            
            for i in range(i,n+1):
                if i not in sol:
                    sol.append(i)
                    backtrack(i+1)
                    sol.pop()
        backtrack(1)
        return res