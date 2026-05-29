class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = 37

        # Traverse through each number in the list
        for num in nums:
            dig = 0

            # Calculate sum of digits of current number
            while num > 0:
                dig += num % 10
                num //= 10

            # Update minimum digit sum
            ans = min(ans, dig)

        return ans