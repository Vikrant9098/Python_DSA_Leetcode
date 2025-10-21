class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]               # Start sequence with 0

        for i in range(n):         # Loop through each bit position
            size = len(result)     # Current size of sequence
            for j in range(size - 1, -1, -1):  # Loop backward through current sequence
                result.append(result[j] | (1 << i))  # Flip the i-th bit and add to sequence

        return result              # Return final gray code sequence
