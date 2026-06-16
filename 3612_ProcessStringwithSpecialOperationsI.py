class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # Initialize an empty string to store the result
        ans = ""

        # Traverse each character in the input string
        for ch in s:

            # If character is '*', remove the last character from ans
            # only if ans is not empty
            if ch == '*' and len(ans) >= 1:
                ans = ans[:-1]

            # If character is '#', duplicate the current string
            # only if ans is not empty
            elif ch == '#' and len(ans) >= 1:
                ans += ans

            # If character is '%', reverse the current string
            elif ch == '%':
                ans = ans[::-1]

            # If the character is a lowercase letter (a-z),
            # append it to the result string
            if 'a' <= ch <= 'z':
                ans += ch

        # Return the final processed string
        return ans