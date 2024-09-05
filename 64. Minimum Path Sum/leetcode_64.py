class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # seen = set()
        # res = []
        # row = len(grid)
        # col =len(grid[0])
        # memo = {}
        # def dfs(x, y, total):
        #     if x < 0 or x >= row or y < 0 or y >= col or (x, y) in seen:
        #         return
            
        #     if x == row-1 and y == col-1:
        #         total += grid[x][y]
        #         res.append(total)
        #         return
            
        #     total += grid[x][y]
        #     seen.add((x, y))

        #     dfs(x+1, y, total)
        #     dfs(x, y+1, total)
        #     seen.remove((x, y))  
        #     return
        
        # dfs(0, 0, 0)
        # return min(res)

        m = len(grid)
        n = len(grid[0])

        dp = [[float("inf") for i in range(n)] for j in range(m)]
        dp[0][0] = grid[0][0]
        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        for i in range(m):
            for j in range(n):
                for x, y in directions:
                    new_x = i + x
                    new_y = j + y
                    if new_x >= 0 and new_x < m and new_y >=0 and new_y < n:
                        dp[i][j] = min(dp[i][j], dp[new_x][new_y]+grid[i][j])
        return dp[m-1][n-1]
    
# my first dp problem solved using tabulation