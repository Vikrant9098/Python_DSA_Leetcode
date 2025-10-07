class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # initialize total sum of all numbers
        total = 0
            
        # initialize maximum subarray sum (non-circular) with first element
        max_sum = nums[0]
        current_max = 0  # current subarray sum for max
        
        # initialize minimum subarray sum (for circular case) with first element
        min_sum = nums[0]
        current_min = 0  # current subarray sum for min
        
        # iterate through each number in array
        for num in nums:
            # find max subarray ending at current number
            current_max = max(num, current_max + num)
            # update global max subarray sum
            max_sum = max(max_sum, current_max)
            
            # find min subarray ending at current number
            current_min = min(num, current_min + num)
            # update global min subarray sum
            min_sum = min(min_sum, current_min)
            
            # accumulate total sum of array
            total += num
        
        # if all numbers are negative, return max_sum
        if max_sum < 0:
            return max_sum
        
        # return max of non-circular or circular subarray sum
        return max(max_sum, total - min_sum)
