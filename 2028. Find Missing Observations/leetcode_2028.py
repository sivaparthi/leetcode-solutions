class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m_total = sum(rolls)
        m = len(rolls)
        n_total = (mean * (m + n)) - m_total
        quotient = n_total // n
        remainder = n_total % n
        res = []
        if quotient > 6 or (quotient == 6 and remainder > 0) or n_total < 0 or quotient == 0:
            return []
        for i in range(n):
            if i < remainder:
                res.append(quotient + 1)
            else:
                res.append(quotient)
        avg = (m_total + sum(res)) / (m + n)
        return res if avg == mean else []