class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        total = sum(chalk)
        sub = (floor(k / total))
        k -= (total * sub)
        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            else:
                k -= chalk[i]
        return i
