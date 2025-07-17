class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        # Stack to store previous strings and repeat counts
        stack = []

        current_string = ""  # Current working string
        num = 0              # Current repeat count

        # Iterate through each character in the string
        for c in s:
            if c.isdigit():
                # If the character is a digit, update the repeat count
                num = num * 10 + int(c)  # Handle multi-digit numbers
            elif c == '[':
                # When we hit '[', push current state to the stack
                stack.append((current_string, num))
                # Reset current string and repeat number for the new block
                current_string = ""
                num = 0
            elif c == ']':
                # When we hit ']', pop from stack and build the repeated string
                prev_string, repeat = stack.pop()
                # Repeat the current string and append it to the previous
                current_string = prev_string + current_string * repeat
            else:
                # For normal letters, just add to the current string
                current_string += c

        return current_string  # Final decoded string
