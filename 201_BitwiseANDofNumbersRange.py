class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        shift = 0  # count how many bits we shift
        
        # Find the common prefix of left and right
        while left < right:
            left >>= 1   # shift both numbers right by 1
            right >>= 1
            shift += 1   # count the shift
        
        # Shift the common bits back to their original position
        return left << shift
