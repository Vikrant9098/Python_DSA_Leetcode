class Solution(object):                 # Define Solution class
    def minPairSum(self, nums):          # Function to find maximum pair sum
        """
        :type nums: List[int]            # Input is a list of integers
        :rtype: int                      # Output is an integer
        """
        min_val, max_val = float('inf'), float('-inf')  # Store min and max values
        freq = [0] * 100001              # Frequency array for numbers

        for i in range(len(nums)):       # Loop through array
            if nums[i] < min_val:        # Check if current is smaller
                min_val = nums[i]        # Update minimum value
            if nums[i] > max_val:        # Check if current is larger
                max_val = nums[i]        # Update maximum value
            freq[nums[i]] += 1           # Increase frequency of number

        max_sum = 0                      # Store maximum pair sum
        l, r = min_val, max_val          # Two pointers from min and max

        while l <= r:                    # Continue while pointers meet
            if freq[l] == 0:             # If no element at l
                l += 1                   # Move left pointer
            elif freq[r] == 0:           # If no element at r
                r -= 1                   # Move right pointer
            else:                        # If both elements exist
                max_sum = max(max_sum, l + r)  # Update max pair sum
                freq[l] -= 1             # Use one l value
                freq[r] -= 1             # Use one r value

        return max_sum                   # Return final answer
