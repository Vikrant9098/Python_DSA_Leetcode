class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        string = ""
        
        # Loop from 1 to n
        for i in range(1, n + 1):
            # Convert number to binary and append to string
            string += format(i, "b")
        
        # Convert final binary string to integer and take modulo
        return int(string, 2) % (10**9 + 7)