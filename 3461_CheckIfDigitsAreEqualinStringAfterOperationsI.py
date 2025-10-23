class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Repeat until only two digits remain
        while len(s) > 2:
            next_s = ""
            # For each consecutive pair of digits
            for i in range(len(s) - 1):
                a = int(s[i])          # Convert current char to int
                b = int(s[i + 1])      # Convert next char to int
                next_s += str((a + b) % 10)  # Append sum modulo 10 as string
            s = next_s  # Update s with the new sequence
        
        # Return True if both digits are same, else False
        return s[0] == s[1]
