class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        cache = {}

        for i in range(len(queries)):
            x, y = queries[i]
            if (x, y) in cache:
                res.append(cache[(x, y)])
                continue
            xor = arr[x]
            for j in range(x+1, y+1):
                xor = xor ^ arr[j]
            cache[(x, y)] = xor
            res.append(xor)
        
        return res