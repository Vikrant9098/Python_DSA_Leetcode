class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Step 1: Remove any trailing spaces at the end of the string
        s = s.rstrip()

        # Step 2: Split the string into words using space as separator
        words = s.split(" ")

        # Step 3: The last word will be at the end of the list
        last_word = words[-1]

        # Step 4: Return the length of the last word
        return len(last_word)
