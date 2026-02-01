class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        # Convert target character to its alphabetical index
        t_ord = ord(target) - ord('a')

        # Loop through each character in letters
        for i in letters:

            # Convert current character to its alphabetical index
            l_ord = ord(i) - ord('a')

            # Check if current character is greater than target
            if l_ord > t_ord:

                # Return the first character greater than target
                return i

        # If no character is greater, return first character (wrap around)
        return letters[0]
