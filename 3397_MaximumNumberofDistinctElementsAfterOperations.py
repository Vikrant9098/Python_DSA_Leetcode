class Solution(object):
    def maxDistinctElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # Sort the numbers in ascending order
        nums.sort()

        # 'last' keeps track of the last distinct number used
        last = float('-inf')

        # 'count' counts the total distinct numbers we can form
        count = 0

        # Loop through each number in the sorted list
        for num in nums:
            # The lowest value we can make from this number
            low = num - k

            # The highest value we can make from this number
            high = num + k

            # Pick the smallest number greater than the previous distinct number
            new_val = max(low, last + 1)

            # Check if this number is within the allowed range
            if new_val <= high:
                # Increase distinct count
                count += 1
                # Update 'last' with the new distinct number
                last = new_val

        # Return the total count of distinct numbers
        return count
