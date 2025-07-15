class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)  # Calculate the total sum of the array
        left_sum = 0  # Initialize the left sum

        for i in range(len(nums)):
            # Right sum can be calculated as total_sum - left_sum - nums[i]
            right_sum = total_sum - left_sum - nums[i]
            
            if left_sum == right_sum:  # Check if left sum equals right sum
                return i  # Return the pivot index
            
            left_sum += nums[i]  # Update the left sum for the next iteration

        return -1  # Return -1 if no pivot index is found
