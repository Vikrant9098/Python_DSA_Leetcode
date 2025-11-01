class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # You lose only when n is a multiple of 4
        # because your opponent can always take enough stones
        # to make the total removed each round equal to 4
        return n % 4 != 0
