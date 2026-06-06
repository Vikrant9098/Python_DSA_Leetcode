class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Calculate the total sum of all elements
        right_sum = sum(nums)

        # Initialize left sum as 0
        left_sum = 0

        # Store the answer for each index
        result = []

        # Traverse through the array
        for num in nums:

            # Remove current element from right sum
            right_sum -= num

            # Store the absolute difference between
            # left sum and right sum
            result.append(abs(left_sum - right_sum))

            # Add current element to left sum
            left_sum += num

        return result