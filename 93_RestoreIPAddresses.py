class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []  # List to store valid IP addresses

        def backtrack(start, path):  # Helper function for recursion
            if len(path) == 4:  # If we already have 4 parts
                if start == len(s):  # And used all digits
                    res.append(".".join(path))  # Join parts and add to result
                return  # Stop recursion

            for l in range(1, 4):  # Try parts of length 1 to 3
                if start + l > len(s):  # If out of bounds
                    break
                part = s[start:start + l]  # Take substring
                if (part.startswith("0") and len(part) > 1) or int(part) > 255:  # Invalid part
                    continue
                backtrack(start + l, path + [part])  # Recurse with next part

        backtrack(0, [])  # Start recursion from index 0
        return res  # Return all valid IPs
