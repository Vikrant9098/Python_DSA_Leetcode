from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # Convert wordList to a set for faster lookup
        word_set = set(wordList)
        
        # If endWord not in wordList, no valid transformation
        if endWord not in word_set:
            return 0
        
        # BFS queue: store (current_word, current_level)
        queue = deque([(beginWord, 1)])
        
        # Visited set to avoid revisiting words
        visited = set([beginWord])
        
        while queue:
            word, level = queue.popleft()
            
            # If reached the endWord, return the level (length of sequence)
            if word == endWord:
                return level
            
            # Try mutating each character
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    # Skip if same character
                    if word[i] == c:
                        continue
                        
                    # Form a new word by changing one character
                    new_word = word[:i] + c + word[i+1:]
                    
                    # If valid and not visited
                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, level + 1))
        
        # If no transformation possible
        return 0
