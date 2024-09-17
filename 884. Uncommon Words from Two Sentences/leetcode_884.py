class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word_list = s1.split(' ')
        word_list2 = s2.split(' ')

        res = []
        hm1 = defaultdict(int)
        for word in word_list:
            hm1[word] += 1
            
        hm2 = defaultdict(int)
        for word in word_list2:
            hm2[word] += 1
        
        for k, v in hm1.items():
            if v == 1 and k not in hm2:
                res.append(k)
        
        for k, v in hm2.items():
            if v == 1 and k not in hm1:
                res.append(k)
        
        return res