class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        ans = [0] * (n + 1)  # store result from 0 to n

        for i in range(1, n + 1):
            # ans[i] = ans[i // 2] + (i % 2)
            # i // 2 shifts the number right (i >> 1)
            # i % 2 adds 1 if last bit is 1
            ans[i] = ans[i >> 1] + (i & 1)

        return ans
