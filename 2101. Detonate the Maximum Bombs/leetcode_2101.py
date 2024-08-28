class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        ranges = {i:[] for i in range(len(bombs))}
        for i in range(len(bombs)):
            x1 , y1, r1 = bombs[i]
            for j in range(len(bombs)):
                if i != j:
                    x2, y2, r2 = bombs[j]
                    d = ((x2-x1)**2 + (y2-y1)**2)**0.5
                    if d <= r1:
                        ranges[i].append(j)
        
        def dfs(bomb, seen):
            if bomb in seen:
                return 0
            ans = 1
            seen.add(bomb)

            for nei in ranges[bomb]:
                ans += dfs(nei, seen)
            return ans
        
        res = float("-inf")
        for i in range(len(bombs)):
            seen = set()
            res = max(res, dfs(i, seen))
        return res

# Calculated the distance between the centers of each circle to determine if they are within range of each other. 
# Then constructed an adj list ans calculated the result 