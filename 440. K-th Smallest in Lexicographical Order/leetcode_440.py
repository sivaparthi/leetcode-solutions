class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        def count(curr):
            res = 0
            nei = curr + 1
            while curr <= n:
                res += min(nei, n+1) - curr
                curr = curr * 10
                nei = nei * 10
            return res

        i = 1
        curr = 1
        while i < k:
            steps = count(curr)
            if i + steps <= k:
                curr += 1
                i += steps
            else:
                curr *= 10
                i += 1
        return curr