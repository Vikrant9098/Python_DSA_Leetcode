class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Use two variables to track the smallest and second smallest values
        # first: smallest value seen so far
        # second: smallest value that is greater than first
        first = float('inf')
        second = float('inf')
        
        # Iterate through the array once
        for num in nums:
            if num <= first:
                # Update first if current number is smaller or equal
                first = num
            elif num <= second:
                # Update second if current number is between first and second
                second = num
            else:
                # Found a number greater than both first and second
                # This means we have an increasing triplet: first < second < num
                return True
        
        # No increasing triplet found
        return False