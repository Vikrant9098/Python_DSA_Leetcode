class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Step 1: Use Floyd's cycle detection algorithm
        slow = nums[0]             # Move one step at a time
        fast = nums[0]             # Move two steps at a time

        # Find the intersection point inside the cycle
        while True:
            slow = nums[slow]          # Move slow by 1 step
            fast = nums[nums[fast]]    # Move fast by 2 steps
            if slow == fast:           # Stop when both meet
                break

        # Step 2: Find the start of the cycle (duplicate number)
        slow = nums[0]             # Move slow pointer back to start
        while slow != fast:        # Move both one step until they meet
            slow = nums[slow]
            fast = nums[fast]

        return slow                # The meeting point is the duplicate number
