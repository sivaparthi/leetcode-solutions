class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # bitmask 😍

        vowels = 'aeiou'
        res = 0
        mask_to_index = {0:-1}
        mask = 0
        for i, c in enumerate(s):
            if c in vowels:
                mask = mask ^ (1 << ord(c)-ord('a'))  # Update bitmask using XOR and bit shifting
                print(mask)
            if mask in mask_to_index:
                res = max(res, i - mask_to_index[mask])
            else:
                mask_to_index[mask] = i
        
        return res