class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        seen = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append([i,j])
                    seen.add((i,j))
        
        ans = -1

        while q:
            r, c = q.popleft()
            ans = grid[r][c]
            directions = [[0,-1], [0, 1], [1,0], [-1,0]]
            for row, col in directions:
                newR = r + row
                newC = c + col
                if newR >= 0 and newR < n and newC >= 0 and newC < n and grid[newR][newC] == 0 and (newR, newC) not in seen:
                    ans = grid[r][c] + 1 
                    grid[newR][newC] = ans
                    q.append([newR, newC])
                    seen.add((newR, newC))
        # print(ans)
        return ans-1 if ans > 1 else -1