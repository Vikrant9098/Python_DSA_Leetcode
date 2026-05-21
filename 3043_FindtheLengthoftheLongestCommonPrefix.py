class Node:
    def __init__(self):
        # Create an array of size 10 for digits 0-9
        self.child = [None] * 10
        
        # Marks the end of a number
        self.isEnd = False


class Solution:

    def insert(self, word, root):
        # Start from the root node
        temp = root

        # Traverse each digit in the word
        for ch in word:
            
            # Convert character digit into index
            idx = ord(ch) - ord('0')

            # Create a new node if path does not exist
            if temp.child[idx] is None:
                temp.child[idx] = Node()

            # Move to the next node
            temp = temp.child[idx]

        # Mark the end of the inserted number
        temp.isEnd = True

    def check(self, string, root):
        # Start traversal from root
        temp = root
        
        # Stores length of matched prefix
        idx = 0

        # Traverse the digits of the string
        while idx < len(string):
            
            # Convert current digit into index
            i = ord(string[idx]) - ord('0')

            # If matching path exists in Trie
            if temp.child[i] is not None:
                
                # Move to next node
                temp = temp.child[i]
                
                # Increase matched prefix length
                idx += 1
            else:
                # Stop if path does not exist
                break

        # Return length of common prefix
        return idx

    def longestCommonPrefix(self, arr1, arr2):
        # Create Trie root node
        root = Node()

        # Insert all numbers from arr2 into Trie
        for x in arr2:
            self.insert(str(x), root)

        # Stores maximum common prefix length
        ans = 0

        # Check each number in arr1
        for x in arr1:
            
            # Update maximum prefix length
            ans = max(ans, self.check(str(x), root))

        # Return final answer
        return ans