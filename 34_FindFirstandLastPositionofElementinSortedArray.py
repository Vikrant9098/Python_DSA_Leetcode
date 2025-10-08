class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Find the first occurrence of target
        first = self.findBound(nums, target, True)
        # If target is not found, return [-1, -1]
        if first == -1:
            return [-1, -1]
        # Find the last occurrence of target
        last = self.findBound(nums, target, False)
        # Return both positions
        return [first, last]

    # Helper function to find first or last occurrence
    def findBound(self, nums, target, isFirst):
        # Initialize left and right pointers
        left, right = 0, len(nums) - 1
        # Store the index of the found boundary
        bound = -1

        # Continue searching while left pointer <= right pointer
        while left <= right:
            # Find middle index
            mid = (left + right) // 2

            # If middle element matches target
            if nums[mid] == target:
                bound = mid  # Store current position
                # If we are finding the first occurrence, move left
                if isFirst:
                    right = mid - 1
                # If we are finding the last occurrence, move right
                else:
                    left = mid + 1
            # If middle value is smaller than target, move right
            elif nums[mid] < target:
                left = mid + 1
            # If middle value is greater than target, move left
            else:
                right = mid - 1

        # Return the found boundary index or -1 if not found
        return bound
