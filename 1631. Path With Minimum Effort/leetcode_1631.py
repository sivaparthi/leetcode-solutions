class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        hq = [(0, (0,0))]
        visit = set()

        while hq:
            effort, cell = heapq.heappop(hq)
            if cell == (rows-1, cols-1):
                return effort
            if cell in visit:
                continue
            visit.add(cell)
            row = cell[0]
            col = cell[1]

            for r, c in directions:
                new_r = row + r
                new_c = col + c
                if (new_r, new_c) not in visit and new_r < rows and new_c < cols and new_r >= 0 and new_c >= 0:
                    new_effort = max(effort, abs(heights[row][col] - heights[new_r][new_c]))
                    heapq.heappush(hq, (new_effort, (new_r, new_c)))            
