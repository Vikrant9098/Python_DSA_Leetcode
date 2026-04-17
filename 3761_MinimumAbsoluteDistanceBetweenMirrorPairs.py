class Solution(object):
    def minMirrorPairDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = dict()          # Stores the last index of reversed numbers
        ans = float('inf')     # Initialize answer with infinity

        for i, num in enumerate(nums):
            # If current number already exists in prev,
            # it means we found a number whose reverse appeared before
            if num in prev:
                # Update minimum distance
                ans = min(ans, i - prev[num])

            # Store the index of the reversed form of current number
            # Example: 123 -> 321
            rev_num = int(str(num)[::-1])
            prev[rev_num] = i

        # If no valid pair found, return -1
        return -1 if ans == float('inf') else ans