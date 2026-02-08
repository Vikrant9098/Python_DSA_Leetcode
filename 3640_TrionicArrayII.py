class Solution(object):                      # Define the Solution class

    def maxSumTrionic(self, nums):            # Function to find max trionic sum
        """
        :type nums: List[int]                # nums is a list of integers
        :rtype: int                          # function returns an integer
        """
        n = len(nums)                        # Store length of array
        res = -float('inf')                  # Store maximum result (start very small)
        i = 1                                # Start index from 1 (middle point)

        while i < n - 2:                     # Loop while enough elements exist
            a = i                            # Left pointer starts at i
            b = i                            # Right pointer starts at i

            net = nums[a]                    # Sum of decreasing middle part

            while b + 1 < n and nums[b + 1] < nums[b]:   # Move right while decreasing
                net += nums[b + 1]           # Add value to middle sum
                b += 1                       # Move right pointer

            if b == a:                       # If no decrease happened
                i += 1                       # Move i forward
                continue                    # Skip this iteration

            c = b                            # Store end of decreasing part

            left = 0                         # Sum of left increasing part
            right = 0                        # Sum of right increasing part
            lx = -float('inf')               # Best left sum
            rx = -float('inf')               # Best right sum

            while a - 1 >= 0 and nums[a - 1] < nums[a]:  # Move left while increasing
                left += nums[a - 1]          # Add value to left sum
                lx = max(lx, left)           # Update best left sum
                a -= 1                       # Move left pointer

            if a == i:                       # If no left increase
                i += 1                       # Move i forward
                continue                    # Skip this iteration

            while b + 1 < n and nums[b + 1] > nums[b]:   # Move right while increasing
                right += nums[b + 1]         # Add value to right sum
                rx = max(rx, right)          # Update best right sum
                b += 1                       # Move right pointer

            if b == c:                       # If no right increase
                i += 1                       # Move i forward
                continue                    # Skip this iteration

            res = max(res, lx + rx + net)    # Update max trionic sum

            i = b                            # Skip already processed elements

        return res if res != -float('inf') else 0  # Return result or 0
