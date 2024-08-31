from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        hm = defaultdict(list)
        
        # Build the graph
        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]
            hm[a].append((b, val))
            hm[b].append((a, 1 / val))
        
        def find_ans(a, b, product):
            if a == b:
                return product
            seen.add(a)
            for denom, val in hm[a]:
                if denom not in seen:
                    result = find_ans(denom, b, product * val)
                    if result != -1:
                        return result
            return -1
        
        ans = []
        for a, b in queries:
            if a not in hm or b not in hm:
                ans.append(-1.0)
            elif a == b:
                ans.append(1.0)
            else:
                seen = set()
                result = find_ans(a, b, 1)
                ans.append(result if result != -1 else -1.0)
        
        return ans
