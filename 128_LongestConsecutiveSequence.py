class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Convert the list to a set for fast O(1) lookups
        num_set = set(nums)
        
        # Variable to keep track of the longest consecutive sequence
        longest = 0

        # Loop through each number in the set
        for num in num_set:
            # Only start counting if num is the start of a sequence
            # (i.e., num-1 is not in the set)
            if num - 1 not in num_set:
                current_num = num        # Current number in the sequence
                current_streak = 1       # Start with a streak of length 1

                # Count consecutive numbers in the sequence
                while current_num + 1 in num_set:
                    current_num += 1      # Move to the next consecutive number
                    current_streak += 1   # Increase the current streak length

                # Update the longest streak found so far
                longest = max(longest, current_streak)

        # Return the length of the longest consecutive sequence
        return longest
