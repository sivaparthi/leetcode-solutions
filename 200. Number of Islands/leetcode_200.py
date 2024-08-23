class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        seen = set()

        def dfs(x, y):
            print((x,y))
            if x >= row or x < 0 or y >= col or y < 0 or (x, y) in seen or grid[x][y] != "1":
                return
            
            seen.add((x, y))
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

            return
        
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in seen:
                    print(i,j)
                    dfs(i, j)
                    count += 1
        
        return count