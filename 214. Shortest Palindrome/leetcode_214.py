class Solution:
    def shortestPalindrome(self, s: str) -> str:
        reversed_string = s[::-1]
        i = 0
        r = len(s) - 1

        longest = 0
        for i in range(len(s)):
            if s[0:i+1] == reversed_string[r:]:
                longest = i
            r -= 1
        
        prefix_to_be_appended = s[longest+1:][::-1]
        return prefix_to_be_appended + s