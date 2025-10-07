class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # initialize current sum and maximum sum with first element
        current_sum = max_sum = nums[0]
        
        # iterate from second element to end
        for num in nums[1:]:
            # either extend the current subarray or start a new one
            current_sum = max(num, current_sum + num)
            
            # update maximum sum if current_sum is larger
            max_sum = max(max_sum, current_sum)
        
        # return the maximum subarray sum
        return max_sum
