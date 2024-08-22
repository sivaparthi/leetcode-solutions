class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        hm = {i:[] for i in range(n)}
        for i in range(n):
            for j in range(n):
                if j != i and isConnected[i][j] == 1:
                    hm[i].append(j)
        ans = 0
        seen = set()
        def dfs(i):
            if i in seen:
                return
            
            seen.add(i)
            for c in hm[i]:
                dfs(c)
            return
        
        for i in range(n):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans

