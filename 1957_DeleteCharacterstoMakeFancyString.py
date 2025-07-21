class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Initialize an empty list to store the final characters of the fancy string
        result = []

        # Iterate through each character in the string
        for char in s:
            # If result has at least two characters and the last two characters are same as current,
            # then skip adding current char to avoid three consecutive same characters
            if len(result) >= 2 and result[-1] == char and result[-2] == char:
                continue

            # Otherwise, add the current character to the result
            result.append(char)

        # Join the list to form the final string and return
        return ''.join(result)
