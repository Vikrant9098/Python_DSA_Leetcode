class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n  # base cases: 1 step -> 1 way, 2 steps -> 2 ways

        first = 1   # ways to reach step 1
        second = 2  # ways to reach step 2

        # Loop from step 3 to n
        for i in range(3, n + 1):
            third = first + second  # current ways = sum of previous two steps
            first = second          # shift first
            second = third          # shift second

        return second  # return ways to reach step n
