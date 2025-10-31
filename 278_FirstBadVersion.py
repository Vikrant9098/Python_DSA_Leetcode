# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n  # define search range
        while left < right:  # binary search loop
            mid = left + (right - left) // 2  # find middle version
            if isBadVersion(mid):  # if mid is bad, move left
                right = mid
            else:  # if mid is good, move right
                left = mid + 1
        return left  # first bad version found
