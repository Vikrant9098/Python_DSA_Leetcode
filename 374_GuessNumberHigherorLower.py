# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Initialize the search boundaries
        low = 1
        high = n

        # Binary search loop to narrow down the correct number
        while low <= high:
            # Find the middle point
            mid = low + (high - low) // 2

            # Call the guess API with the middle number
            res = guess(mid)

            # If the guess is correct, return the number
            if res == 0:
                return mid
            # If our guess is higher than the picked number,
            # discard the right half
            elif res == -1:
                high = mid - 1
            # If our guess is lower than the picked number,
            # discard the left half
            else:
                low = mid + 1

        # This line will never be reached because the number is guaranteed to exist
        return -1
