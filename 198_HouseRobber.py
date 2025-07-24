class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Edge case: If there's only one house, rob it.
        if len(nums) == 1:
            return nums[0]

        # Edge case: If there are only two houses, rob the one with more money.
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # Initialize two variables:
        # prev1: max money robbed till the previous house (i - 1)
        # prev2: max money robbed till the house before that (i - 2)
        prev2 = nums[0]        # Only one house, rob it
        prev1 = max(nums[0], nums[1])  # Rob the house with more money among first two

        # Loop through the remaining houses starting from index 2
        for i in range(2, len(nums)):
            # Decide whether to rob the current house or not:
            # If we rob it, we add its value to prev2 (non-adjacent)
            # If we skip it, we take prev1 (which is max till previous house)
            current = max(prev1, nums[i] + prev2)

            # Update prev2 and prev1 for the next iteration
            prev2 = prev1
            prev1 = current

        # After looping through all houses, prev1 holds the max money that can be robbed
        return prev1
