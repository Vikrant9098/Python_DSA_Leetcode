class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Stack to keep track of expected closing brackets
        stack = []

        # Iterate through each character in the string
        for c in s:
            # If the character is an opening bracket '('
            if c == '(':
                stack.append(')')  # Push the corresponding closing bracket
            # If the character is an opening bracket '{'
            elif c == '{':
                stack.append('}')  # Push the corresponding closing bracket
            # If the character is an opening bracket '['
            elif c == '[':
                stack.append(']')  # Push the corresponding closing bracket
            # If the character is a closing bracket
            else:
                # Check if stack is empty or top does not match
                if not stack or stack.pop() != c:
                    return False  # Invalid string, mismatch found

        # If stack is empty at the end, all brackets matched
        return not stack
