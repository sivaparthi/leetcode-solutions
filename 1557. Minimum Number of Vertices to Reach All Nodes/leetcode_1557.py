class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        hm = {i:[] for i in range(n)}
        for u, v in edges:
            hm[v].append(u)
        
        res = []
        for k, v in hm.items():
            if v == []:
                res.append(k)
        
        return res