class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])

        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]!='1':
                return
            else:
                grid[i][j]='0'
                dfs(i,j+1)#right
                dfs(i+1,j)#down
                dfs(i,j-1)#left
                dfs(i-1,j)#up
        
        num_islands=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    num_islands+=1
                    dfs(i,j)
        return num_islands