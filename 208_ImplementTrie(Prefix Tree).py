class TrieNode(object):
    def __init__(self):
        # Each node has a dictionary to store children and a flag to indicate the end of a word
        self.children = {}
        self.is_end_of_word = False


class Trie(object):

    def __init__(self):
        # Initialize the root node of the trie
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root  # Start from the root node

        for char in word:
            # If the character is not already a child of the current node, create a new node
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]  # Move to the child node

        node.is_end_of_word = True  # Mark the last node as the end of a valid word

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root  # Start from the root

        for char in word:
            # If the character is not found in children, return False
            if char not in node.children:
                return False
            node = node.children[char]  # Move to the next node

        # Return True only if this is the end of a valid word
        return node.is_end_of_word

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root  # Start from the root

        for char in prefix:
            # If character path doesn't exist, prefix not found
            if char not in node.children:
                return False
            node = node.children[char]  # Move to the next node

        return True  # All characters of prefix found, return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
