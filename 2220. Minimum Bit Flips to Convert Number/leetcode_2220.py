class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        num_1 = bin(start)[2:]
        num_2 = bin(goal)[2:]
        max_len = max(len(num_1), len(num_2))
        if len(num_1) < max_len:
            num_1_len = len(num_1)
            while num_1_len < max_len:
                num_1 = '0' + num_1
                num_1_len = len(num_1)
        if len(num_2) < max_len:
            num_2_len = len(num_2)
            while num_2_len < max_len:
                num_2 = '0' + num_2
                num_2_len = len(num_2)
        
        ans = 0
        for i in range(len(num_1)):
            if num_1[i] != num_2[i]:
                ans += 1
        
        return ans