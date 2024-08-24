class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        hm = {i+1:[] for i in range(n)}
        for k,v in trust:
            # print(k, v)
            hm[k].append(v)
        for i in range(n):
            if hm[i+1] == []:
                flag = True
                for k, v in hm.items():
                    if k != i+1 and i+1 not in v:
                        flag = False
                        break
                if flag:
                    return i+1
        return -1
    
