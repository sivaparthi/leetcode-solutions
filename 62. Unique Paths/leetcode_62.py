class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # count = [0]
        cache = defaultdict(int)

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    cache[(i, j)] = 1
        
        # def dfs(x, y):
        #     if x < 0 or x >= m or y < 0 or y >= n:
        #         return

        #     # cache[(x, y)] += 
        #     if (x, y) == (m-1, n-1):
        #         count[0] += 1

        #     dfs(x+1, y)
        #     dfs(x, y+1)

        
        # dfs(0, 0)
        # print(cache)
        # return count[0]

        for i in range(1, m):
            for j in range(1, n):
                cache[(i, j)] = cache[(i, j-1)] + cache[(i-1, j)]
        
        return cache[(m-1, n-1)]