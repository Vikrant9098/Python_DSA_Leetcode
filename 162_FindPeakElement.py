class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Initialize binary search boundaries
        low = 0
        high = len(nums) - 1

        # Binary search loop
        while low < high:
            # Find the middle index
            mid = low + (high - low) // 2

            # Compare mid element with its right neighbor
            if nums[mid] > nums[mid + 1]:
                # If mid element is greater than right neighbor,
                # then peak lies on the left side (including mid)
                high = mid
            else:
                # If right neighbor is greater,
                # then peak lies on the right side (excluding mid)
                low = mid + 1

        # When low == high, we have found a peak element
        return low
