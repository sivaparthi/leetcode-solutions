class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        adj_list = defaultdict(list)

        def generate_neighbors(word):
            neighbors = []
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':  # Try every letter in the alphabet
                    new_word = word[:i] + char + word[i+1:]  # Change one letter at a time
                    if new_word != word and new_word in wordSet:
                        neighbors.append(new_word)
            return neighbors

        for word in wordList:
            adj_list[word] = generate_neighbors(word)

        adj_list[beginWord] = generate_neighbors(beginWord)

        q = deque()
        q.append((beginWord, 1))
        seen = set()

        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            if word in seen:
                continue
            seen.add(word)

            for nei in adj_list[word]:
                if nei not in seen:
                    q.append((nei, steps + 1))
        
        return 0