class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """

        n = len(nums)

        # Difference array to track changes in operations count
        diff = [0] * (2 * limit + 2)

        # Process each pair from both ends of the array
        for i in range(n // 2):

            # Smaller value in the pair
            a = min(nums[i], nums[n - 1 - i])

            # Larger value in the pair
            b = max(nums[i], nums[n - 1 - i])

            # By default, every sum needs 2 operations
            diff[2] += 2

            # From (a + 1), only 1 operation is needed
            diff[a + 1] -= 1

            # At exact sum (a + b), 0 operations are needed
            diff[a + b] -= 1

            # After (a + b), operations increase again
            diff[a + b + 1] += 1

            # After (b + limit), 2 operations are needed again
            diff[b + limit + 1] += 1

        # Store minimum operations answer
        min_ops = n

        # Current operations count while scanning sums
        current_ops = 0

        # Check all possible pair sums
        for c in range(2, 2 * limit + 1):

            # Apply difference array changes
            current_ops += diff[c]

            # Update minimum operations if smaller value found
            if current_ops < min_ops:
                min_ops = current_ops

        # Return minimum moves required
        return min_ops