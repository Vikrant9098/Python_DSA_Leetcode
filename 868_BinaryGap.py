class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Convert number into binary string (example: 9 -> '0b1001')
        binary_string = bin(n)

        # p1 will store position of previous '1'
        # p2 will store position of current '1'
        p1, p2 = 0, 0

        # dtc (distance) will store the maximum gap found
        dtc = 0

        # Start from index 2 because binary string starts with '0b'
        for i in range(2, len(binary_string)):

            # If current character is '1'
            if binary_string[i] == '1':

                # If this is the first '1' we found
                if p1 == 0:
                    p1 = i  # Store its position

                else:
                    # If we already found a '1' before
                    p2 = i  # Store current position

                    # Calculate distance between two 1's
                    # and keep the maximum distance
                    dtc = max((p2 - p1), dtc)

                    # Update p1 to current position
                    # so we can compare with next '1'
                    p1 = p2

        # Return the largest distance found
        return dtc