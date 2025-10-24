from collections import defaultdict, deque  # Import data structures for adjacency list and BFS queue

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        # 1. Create adjacency list based on patterns
        def adjacencyList():
            adj = defaultdict(list)           # Initialize adjacency list
            for word in wordList:             # Iterate through all words
                for i, _ in enumerate(word):  # Iterate through each character
                    pattern = word[:i] + "*" + word[i + 1 :]  # Replace char with '*'
                    adj[pattern].append(word)  # Group words by pattern
            return adj                        # Return adjacency list

        # 2. BFS to build reversed adjacency list
        def bfs(adj):
            reversedAdj = defaultdict(list)   # Initialize reversed adjacency list
            queue = deque([beginWord])        # Queue for BFS starting with beginWord
            visited = set([beginWord])        # Keep track of visited words

            while queue:                      # While queue is not empty
                visitedCurrentLevel = set()   # Track visited words at current level
                n = len(queue)                # Number of words at this level
                for _ in range(n):
                    word = queue.popleft()    # Pop word from front of queue
                    for i, _ in enumerate(word):  # Iterate through each char
                        pattern = word[:i] + "*" + word[i + 1 :]  # Generate pattern
                        for nextWord in adj[pattern]:             # Iterate neighbors
                            if nextWord not in visited:          # If not visited before
                                reversedAdj[nextWord].append(word)  # Add edge in reversed graph
                                if nextWord not in visitedCurrentLevel:  # If not visited this level
                                    queue.append(nextWord)      # Add to BFS queue
                                    visitedCurrentLevel.add(nextWord)  # Mark visited this level
                visited.update(visitedCurrentLevel)  # Add current level words to visited
                if endWord in visited:                 # Stop if endWord is reached
                    break
            return reversedAdj                         # Return reversed adjacency list

        # 3. DFS to construct all shortest paths
        def dfs(reversedAdj, res, path):
            if path[0] == beginWord:                  # Base case: reached start
                res.append(list(path))                # Add path to result
                return res
            word = path[0]                             # Get current word
            for nextWord in reversedAdj[word]:         # Iterate neighbors in reversed graph
                path.appendleft(nextWord)             # Add neighbor to start of path
                dfs(reversedAdj, res, path)           # Recursively DFS
                path.popleft()                         # Remove neighbor after DFS
            return res                                 # Return result

        # Run all three steps
        adj = adjacencyList()                           # Step 1: adjacency list
        reversedAdj = bfs(adj)                          # Step 2: BFS reversed adjacency
        res = dfs(reversedAdj, [], deque([endWord]))   # Step 3: DFS to construct paths
        return res                                      # Return all shortest paths
