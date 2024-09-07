class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # count = [0]
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        cache = defaultdict(int)

        if obstacleGrid[0][0] == 1:
            return 0
        else:
            cache[(0, 0)] = 1
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j > 0:
                    if obstacleGrid[i][j] == 1:
                        cache[(i, j)] = 0
                    elif cache[(i, j-1)] != 0:
                        cache[(i, j)] = 1
                    else:
                        cache[(i, j)] = 0
                if j == 0 and i > 0:
                    if obstacleGrid[i][j] == 1:
                        cache[(i, j)] = 0
                    elif cache[(i-1, j)] != 0:
                        cache[(i, j)] = 1
                    else:
                        cache[(i, j)] = 0
                    
        print(cache)
            
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    cache[(i, j)] = 0
                else:
                    cache[(i, j)] = cache[(i-1, j)] + cache[(i, j-1)]
        return cache[(m-1, n-1)]

        # def dfs(x, y):
        #     if  x < 0 or x >= m or y < 0 or y >= n or obstacleGrid[x][y] == 1:
        #         return

        #     cache[(x, y)] += 1
        #     if (x, y) == (m-1, n-1):
        #         count[0] += 1
            
        #     dfs(x+1, y)
        #     dfs(x, y+1)

        # dfs(0, 0)
        # print(cache)
        # return count[0]