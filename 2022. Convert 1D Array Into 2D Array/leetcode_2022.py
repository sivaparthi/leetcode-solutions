class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []

        res = []
        i = 0
        j = 0
        ans = []
        while i < len(original):
            if j < n:
                ans.append(original[i])
                j += 1
            else:
                j = 1
                res.append(ans)
                ans = []
                ans.append(original[i])
        
            i += 1
        res.append(ans)
        print(res)
        return res
        