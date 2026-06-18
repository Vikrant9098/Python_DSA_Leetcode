class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        # First pass:
        # Calculate the final length of the string after applying all operations.
        length = 0

        for c in s:

            # '*' removes the last character (if any exists)
            if c == "*":
                if length:
                    length -= 1

            # '#' duplicates the current string,
            # so its length becomes twice the current length
            elif c == "#":
                length *= 2

            # '%' reverses the string.
            # Reversing does not change the length.
            elif c == "%":
                pass

            # Any lowercase letter is appended to the string
            else:
                length += 1

        # If k is outside the final string length,
        # return '.'
        if k + 1 > length:
            return "."

        # Second pass (Reverse Processing):
        # Instead of constructing the whole string,
        # we trace backwards to find which character
        # ends up at index k.
        for c in reversed(s):

            # Reverse effect of '*'
            # Before deletion, string length was one more.
            if c == "*":
                length += 1

            # Reverse effect of '#'
            elif c == "#":

                # Before duplication:
                # original length = current_length / 2
                original_length = (length + 1) // 2

                # If k lies in the duplicated second half,
                # map it back to the corresponding position
                # in the first half.
                if k + 1 > original_length:
                    k -= length // 2

                # Restore original length
                length = original_length

            # Reverse effect of '%'
            elif c == "%":

                # If a string of size 'length' was reversed,
                # index k originally came from:
                # length - k - 1
                k = length - k - 1

            # Current character is a normal letter
            else:

                # During forward processing this character
                # was appended at position (length - 1).
                # If k points to that position,
                # we found our answer.
                if k + 1 == length:
                    return c

                # Remove this character and continue
                # tracing backwards.
                length -= 1

        # Safety fallback (should never be reached)
        return "."