class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0            # total count of 1s
        factor = 1           # current digit position (1, 10, 100, ...)

        while factor <= n:
            lower = n % factor                  # digits to the right
            curr = (n // factor) % 10           # current digit
            higher = n // (factor * 10)         # digits to the left

            if curr == 0:
                count += higher * factor         # no extra 1s from this position
            elif curr == 1:
                count += higher * factor + lower + 1  # include partial range
            else:
                count += (higher + 1) * factor   # full range contributes 1s

            factor *= 10                         # move to next digit position

        return count                             # total count of 1s
