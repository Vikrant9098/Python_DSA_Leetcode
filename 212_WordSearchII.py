class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        # Define a TrieNode class for building a Trie
        class TrieNode(object):
            def __init__(self):
                self.children = {}  # Dictionary to store child nodes
                self.isEndOfWord = False  # Flag to mark end of a word

        # Build a Trie from the list of words
        root = TrieNode()  # Root of Trie
        for word in words:  # Loop through each word
            node = root  # Start from root for each word
            for char in word:  # Loop through each character
                if char not in node.children:  # If character not in children
                    node.children[char] = TrieNode()  # Create a new TrieNode
                node = node.children[char]  # Move to the child node
            node.isEndOfWord = True  # Mark the last node as end of word

        m, n = len(board), len(board[0])  # Dimensions of the board
        result = set()  # Set to store found words (avoid duplicates)

        # DFS function to explore the board
        def dfs(i, j, node, path):
            if i < 0 or i >= m or j < 0 or j >= n:  # Check boundaries
                return
            char = board[i][j]  # Current character
            if char not in node.children:  # If char not in current Trie node
                return
            node = node.children[char]  # Move to the next Trie node
            path += char  # Add char to current path
            if node.isEndOfWord:  # If path forms a word in Trie
                result.add(path)  # Add word to result set

            board[i][j] = '#'  # Mark current cell as visited

            # Explore all 4 directions: down, up, right, left
            dfs(i+1, j, node, path)
            dfs(i-1, j, node, path)
            dfs(i, j+1, node, path)
            dfs(i, j-1, node, path)

            board[i][j] = char  # Restore the cell after DFS

        # Start DFS from every cell in the board
        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "")  # DFS with empty path starting at (i,j)

        return list(result)  # Return all found words as a list
