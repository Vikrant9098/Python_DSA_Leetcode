class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sort the array so we can use two-pointer method
        nums.sort()

        # Variable to store the count of valid triangles
        count = 0

        # Loop from the last element (largest side of triangle)
        for k in range(len(nums) - 1, 1, -1):
            # Two pointers: i starts at 0, j just before k
            i, j = 0, k - 1

            # While left pointer is less than right pointer
            while i < j:
                # If nums[i] + nums[j] > nums[k], it forms a valid triangle
                if nums[i] + nums[j] > nums[k]:
                    # All pairs from i..j-1 with j are valid
                    count += (j - i)
                    # Move j left
                    j -= 1
                else:
                    # Otherwise move i right
                    i += 1

        # Return the total count
        return count
