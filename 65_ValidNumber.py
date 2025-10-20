class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()  # Remove leading and trailing spaces
        num_seen = False   # Flag: True if at least one digit is seen
        dot_seen = False   # Flag: True if '.' is seen
        e_seen = False     # Flag: True if 'e' or 'E' is seen

        for i, c in enumerate(s):
            if c.isdigit():
                num_seen = True  # Digit found, mark num_seen True
            elif c == '.':
                if dot_seen or e_seen:
                    return False  # '.' cannot appear twice or after 'e'
                dot_seen = True  # Mark that dot is seen
            elif c in ('e', 'E'):
                if e_seen or not num_seen:
                    return False  # 'e' must appear once and after number
                e_seen = True     # Mark that exponent is seen
                num_seen = False  # Reset num_seen for digits after exponent
            elif c in ('+', '-'):
                if i != 0 and s[i-1] not in ('e', 'E'):
                    return False  # '+'/'-' only at start or after 'e'
            else:
                return False  # Any other character is invalid

        return num_seen  # True if at least one digit exists in the end
