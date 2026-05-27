class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """

        # Create a 2D list to store lowercase and uppercase presence
        # A[i][0] -> lowercase character exists
        # A[i][1] -> uppercase character exists
        # Index 1-26 represent letters a-z
        A = [[False, False] for _ in range(27)]

        # Traverse each character in the word
        for ch in word:

            # Get alphabet position (1-26)
            # Example:
            # 'a' or 'A' -> 1
            # 'b' or 'B' -> 2
            i = ord(ch) & 31

            # Determine character type
            # 1 -> uppercase
            # 0 -> lowercase
            c = (ord(ch) >> 5) & 1

            # Update character presence
            # If uppercase comes after lowercase, mark uppercase as True
            # If uppercase appears before lowercase, it should not count
            A[i][c] = not (c and A[i][0])

        # Count characters where both lowercase and uppercase exist
        return sum(lower and upper for lower, upper in A)