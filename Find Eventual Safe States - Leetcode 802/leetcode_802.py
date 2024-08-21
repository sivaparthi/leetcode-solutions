class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        hm = {i:[] for i in range(len(graph))}
        for i, l in enumerate(graph):
            hm[i] = l
        
        seen = set()
        cache = {}
        def dfs(node):
            if node in seen:
                return False
            if node in cache:
                return cache[node]
            if hm[node] == []:
                return True
            
            seen.add(node)

            for n in hm[node]:
                if not dfs(n):
                    cache[n] = False
                    return cache[n]
            cache[node] = True
            seen.remove(node)
            return cache[node]
        
        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res
    
    # Time complexity --> O(V+E)
    # Topological sort