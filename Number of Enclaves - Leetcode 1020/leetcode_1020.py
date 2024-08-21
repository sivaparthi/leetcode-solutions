class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        seen = set()

        def dfs(x, y):
            if x < 0 or x >= row or y < 0 or y >= col or (x, y) in seen or grid[x][y] == 0:
                return
            
            seen.add((x, y))
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
            
            return
        
        for i in range(row):
            for j in range(col):
                if i == 0 or i == row-1 or j == 0 or j == col-1:
                    dfs(i, j)

        ans = 0
        for i in range(row):
            for j in range(col):
                if (i, j) not in seen and grid[i][j] == 1:
                    ans += 1
        
        return ans
    
# DFS