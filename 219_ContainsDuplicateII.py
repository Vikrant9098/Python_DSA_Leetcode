class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}  # Dictionary to store number -> last index

        for i, num in enumerate(nums):
            # If number was seen before and distance between indices <= k
            if num in seen and i - seen[num] <= k:
                return True

            # Update last index of the number
            seen[num] = i

        # No such pair found
        return False
