class TrieNode(object):
    __slots__ = ['children', 'bestLen', 'bestIdx']

    def __init__(self):
        # Dictionary to store child nodes
        self.children = {}

        # Stores the smallest word length passing through this node
        self.bestLen = float('inf')

        # Stores index of the smallest word
        self.bestIdx = float('inf')


class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        """
        :type wordsContainer: List[str]
        :type wordsQuery: List[str]
        :rtype: List[int]
        """

        # Create root node of Trie
        root = TrieNode()

        # Insert all words into Trie in reverse order
        for i, word in enumerate(wordsContainer):

            n = len(word)
            curr = root

            # Update root with best word info
            if n < curr.bestLen or (n == curr.bestLen and i < curr.bestIdx):
                curr.bestLen = n
                curr.bestIdx = i

            # Insert characters from end to start
            for char in reversed(word):

                # Create new node if character not present
                if char not in curr.children:
                    curr.children[char] = TrieNode()

                # Move to next node
                curr = curr.children[char]

                # Update best word information at current node
                if n < curr.bestLen or (n == curr.bestLen and i < curr.bestIdx):
                    curr.bestLen = n
                    curr.bestIdx = i

        # Store final answers
        ans = []

        # Process each query word
        for query in wordsQuery:

            curr = root

            # Traverse Trie using reversed query
            for char in reversed(query):

                # Stop if matching suffix path not found
                if char not in curr.children:
                    break

                curr = curr.children[char]

            # Append best matching word index
            ans.append(curr.bestIdx)

        return ans