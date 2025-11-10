class Solution(object):
    def minOperations(self, nums):
        ans = 0                              # Count of total operations
        seen = [False] * 100001              # Track which numbers have been seen
        mono_stack = [0] * len(nums)         # Stack to maintain increasing order
        top = 0                              # Points to current top of stack

        for curr in nums:                    # Loop through all numbers in nums
            if curr == 0:                    # If current number is zero
                while top > 0:               # Clear the stack
                    top -= 1
                    seen[mono_stack[top]] = False  # Mark number as unseen
                continue                     # Move to next number

            # Remove larger elements to maintain increasing order
            while top > 0 and mono_stack[top - 1] > curr:
                top -= 1
                seen[mono_stack[top]] = False  # Mark removed element as unseen

            # If current number is not seen before
            if not seen[curr]:
                ans += 1                      # New operation needed
                seen[curr] = True             # Mark number as seen

            mono_stack[top] = curr            # Push current number to stack
            top += 1                          # Increase stack pointer

        return ans                            # Return total operations
