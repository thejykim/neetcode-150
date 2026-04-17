from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        patterns = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i+1:]
                patterns[key].append(word)
        
        visited = set()
        queue = deque()
        queue.append(beginWord)
        dist = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return dist

                if word in visited:
                    continue
                
                visited.add(word)

                for i in range(len(word)):
                    key = word[:i] + '*' + word[i+1:]
                    for neighbor in patterns[key]:
                        if neighbor != word:
                            queue.append(neighbor)
            
            dist += 1
        
        return 0