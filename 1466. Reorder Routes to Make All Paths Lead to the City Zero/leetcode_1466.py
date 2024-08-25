class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        neigh = {i:[] for i in range(n)}
        for i, j in connections:
            neigh[i].append(j)
            neigh[j].append(i)
        
        hm = {i:[] for i in range(n)}
        for i, j in connections:
            hm[i].append(j)
        
        ans = 0
        q = deque()
        q.append(0)
        seen = set()
        
        while q:
            city = q.pop()
            seen.add(city)
            for nei in neigh[city]:
                if nei not in seen:
                    if city not in hm[nei]:
                        ans +=1
                    q.append(nei)
        
        return ans