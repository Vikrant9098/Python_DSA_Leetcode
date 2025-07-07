class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # Get the length of first string
        m = len(word1)
        # Get the length of second string
        n = len(word2)
        # Set loop count to the maximum length of both strings
        loopcount = max(m,n)
        # Initialize empty string to store the result
        result = ''
        
        # Loop from 0 to the maximum length of both strings
        for i in range(loopcount):
            # Check if current index is within bounds of word1
            if i < m:
                # Add character from word1 at current index to result
                result += word1[i]

            # Check if current index is within bounds of word2
            if i < n:   
                # Add character from word2 at current index to result
                result += word2[i]

        # Print the final merged string (for debugging)
        print(result)
        # Return the final merged string
        return result