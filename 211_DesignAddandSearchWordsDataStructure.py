class WordDictionary(object):

    # Trie Node definition
    class TrieNode(object):
        def __init__(self):
            self.children = {}  # Dictionary to store children nodes
            self.isEndOfWord = False  # Flag to mark end of a word

    def __init__(self):
        """
        Initialize the root of Trie
        """
        self.root = self.TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root  # Start from root
        for char in word:
            if char not in node.children:  # If child node doesn't exist
                node.children[char] = self.TrieNode()  # Create new node
            node = node.children[char]  # Move to next node
        node.isEndOfWord = True  # Mark the last node as end of word

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(node, i):
            if i == len(word):  # Reached end of search word
                return node.isEndOfWord  # Return True if it's a complete word
            
            char = word[i]
            if char == '.':  # Wildcard, check all possible children
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False  # No match found
            else:
                if char in node.children:
                    return dfs(node.children[char], i + 1)  # Move to next character
                else:
                    return False  # Character not found

        return dfs(self.root, 0)  # Start DFS from root


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
