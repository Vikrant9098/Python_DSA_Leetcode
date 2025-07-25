class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """

        flips = 0  # total number of flips needed

        # loop through all 32 bits (since numbers are <= 10^9)
        for i in range(32):
            
            # get the i-th bit of a using right shift and bit AND
            abit = (a >> i) & 1

            # get the i-th bit of b
            bbit = (b >> i) & 1

            # get the i-th bit of c
            cbit = (c >> i) & 1

            # if (abit OR bbit) doesn't match cbit, flip is needed
            if (abit | bbit) != cbit:

                if cbit == 1:
                    # if c's bit is 1 but both a and b bits are 0
                    # we need 1 flip (either a or b to 1)
                    flips += 1
                else:
                    # if c's bit is 0, flip all 1s in a and b to 0
                    flips += abit + bbit  # add 1 for each 1

        return flips  # return total number of flips
