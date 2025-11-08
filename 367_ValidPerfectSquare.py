class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 1, num              # search range between 1 and num

        while left <= right:              # continue while search space exists
            mid = (left + right) // 2     # find the middle number
            square = mid * mid            # calculate mid^2

            if square == num:             # if perfect square found
                return True
            elif square < num:            # if mid^2 is smaller, move right
                left = mid + 1
            else:                         # if mid^2 is larger, move left
                right = mid - 1

        return False                      # not a perfect square
