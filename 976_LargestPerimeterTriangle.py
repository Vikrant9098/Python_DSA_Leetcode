class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sort the array in non-decreasing order
        nums.sort()
        
        # Start checking from the largest side
        for i in range(len(nums) - 1, 1, -1):
            # Check if the three sides can form a valid triangle
            if nums[i - 2] + nums[i - 1] > nums[i]:
                # Return the perimeter if valid
                return nums[i - 2] + nums[i - 1] + nums[i]
        
        # If no valid triangle found, return 0
        return 0
