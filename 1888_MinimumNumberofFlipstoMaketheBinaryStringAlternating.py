class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n = len(s)
        
        # Duplicate the string to simulate all possible rotations
        t = s + s
        
        # Initialize answer with maximum possible flips
        ans = n
        
        # Count mismatches for pattern starting with '0'
        mis0 = 0

        # Traverse the virtual string of length 2*n
        for i in range(2 * n):

            # Expected character if pattern starts with '0'
            expected0 = '0' if i % 2 == 0 else '1'

            # If current character does not match expected pattern, increase mismatch
            if t[i] != expected0:
                mis0 += 1

            # Maintain sliding window of size n
            if i >= n:
                left = i - n

                # Expected character for the leftmost element leaving the window
                exp_left = '0' if left % 2 == 0 else '1'

                # If it was contributing to mismatch, remove it
                if t[left] != exp_left:
                    mis0 -= 1

            # When window size becomes n, compute flips
            if i >= n - 1:
                # Flips required if pattern starts with '1'
                mis1 = n - mis0

                # Take minimum flips
                ans = min(ans, min(mis0, mis1))

        return ans