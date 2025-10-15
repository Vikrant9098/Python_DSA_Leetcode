class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0  # store the maximum valid length
        stack = [-1]  # stack stores indices, start with -1 as base

        for i in range(len(s)):  # loop through each character
            if s[i] == '(':  
                stack.append(i)  # push index of '('
            else:
                stack.pop()  # pop one element for matching ')'
                if not stack:
                    stack.append(i)  # push current index as new base if stack empty
                else:
                    # calculate length of current valid substring
                    max_len = max(max_len, i - stack[-1])

        return max_len  # return the maximum valid length found
