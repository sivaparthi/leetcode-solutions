class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(i for i in allowed)
        count = 0
        
        for word in words:
            countable = True
            for i in word:
                if i not in allowed_set:
                    countable = False
                    break
            if countable:
                count += 1

        return count