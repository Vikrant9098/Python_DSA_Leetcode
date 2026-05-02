class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Initialize count of good numbers
        count = 0

        # Iterate from 1 to n
        for num in range(1, n + 1):
            s = str(num)

            # Check if number contains at least one valid rotating digit (2,5,6,9)
            has_valid_rotation = any(c in '2569' for c in s)

            # Check if number contains any invalid digit (3,4,7)
            has_invalid_digit = any(c in '347' for c in s)

            # A number is good if it has valid rotation and no invalid digit
            if has_valid_rotation and not has_invalid_digit:
                count += 1

        return count