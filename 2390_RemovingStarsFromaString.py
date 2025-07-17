class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Use a list as a stack to keep track of characters
        stack = []

        # Iterate through each character in the input string
        for char in s:
            if char == '*':
                # If the character is '*', pop the last character from the stack
                # This simulates removing the closest non-star to the left
                if stack:
                    stack.pop()
            else:
                # If it's a normal character, push it onto the stack
                stack.append(char)

        # Join the stack to get the final result string
        return ''.join(stack)
