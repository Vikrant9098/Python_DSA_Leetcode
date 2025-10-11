class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # If x is 0 or 1, return x directly
        if x < 2:
            return x

        # Initialize binary search boundaries
        left, right = 1, x // 2
        ans = 0

        # Binary search to find integer square root
        while left <= right:
            mid = (left + right) // 2  # middle value
            square = mid * mid  # calculate square

            if square == x:
                return mid  # perfect square found
            elif square < x:
                ans = mid  # store possible answer
                left = mid + 1  # move right
            else:
                right = mid - 1  # move left

        # Return the floor value of square root
        return ans
