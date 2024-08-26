class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1], [1, 1], [-1, -1], [1,-1], [-1, 1]]
        seen = set()
        q = deque()
        ans = 1 
        if grid[0][0] == 0 and row == 1 and col == 1:
            return ans
        if grid[0][0] == 0:
            q.append((0,0))
            seen.add((0,0))
        else:
            return -1
        while q:
            ans += 1
            for i in range(len(q)):
                x, y = q.popleft()
                for r, c in directions:
                    new_x = x + r
                    new_y = y + c
                    print((new_x, new_y))
                    if new_x < row and new_x >= 0 and new_y < col and new_y >=0 and (new_x, new_y) not in seen:
                        if grid[new_x][new_y] == 0 and (new_x, new_y) == (row-1, col-1):
                            return ans
                        if grid[new_x][new_y] == 0 and (new_x, new_y) not in seen:
                            seen.add((new_x, new_y))
                            q.append((new_x, new_y))
        return -1
    
# not the cleanest code 😪