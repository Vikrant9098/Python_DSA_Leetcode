class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # base cases
        if n == 2:
            return 1  # 1 + 1 -> 1 * 1 = 1
        if n == 3:
            return 2  # 1 + 2 -> 1 * 2 = 2

        product = 1  # to store result

        # keep subtracting 3 to get max product
        while n > 4:
            product *= 3  # multiply by 3
            n -= 3        # reduce n by 3

        # multiply remaining part (2, 3, or 4)
        product *= n

        return product  # return final product
