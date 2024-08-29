class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        hm = {i:[] for i in range(len(stones))}
        for i in range(len(stones)):
            x1, y1 = stones[i]
            for j in range(len(stones)):
                if i != j:
                    x2, y2 = stones[j]
                    if x1 == x2 or y1 == y2:
                        hm[i].append(j)
        
        def dfs(stone):
            if stone in seen:
                return 0
            
            seen.add(stone)
            ans = 1

            for j in hm[stone]:
                ans += dfs(j)
            
            return ans

        seen = set()
        res = 0
        for i in range(len(stones)):
            if i not in seen:
                res += dfs(i) - 1
        return res

# Used dfs. But I think Disjoint sets can be used to solve with a better time.