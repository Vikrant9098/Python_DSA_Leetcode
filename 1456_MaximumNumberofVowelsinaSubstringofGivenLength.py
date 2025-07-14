class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Sliding window approach
        # Calculate sum of first k elements
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Slide window: remove first element, add next element
        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, current_sum)
        
        # Return maximum average
        return max_sum / float(k)
    
    # Alternative explicit sliding window
    def findMaxAverage_v2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Calculate first window sum
        window_sum = 0
        for i in range(k):
            window_sum += nums[i]
        
        max_sum = window_sum
        
        # Slide window from position k to end
        for i in range(k, len(nums)):
            # Remove leftmost element, add rightmost element
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
        
        return max_sum / float(k)

# Logic:
# 1. Calculate sum of first k elements (initial window)
# 2. Slide window: remove left element, add right element
# 3. Track maximum sum found across all windows
# 4. Return max_sum / k as the maximum average

# Test examples:
# nums = [1,12,-5,-6,50,3], k = 4
# Window 1: [1,12,-5,-6] → sum = 2
# Window 2: [12,-5,-6,50] → sum = 51 (maximum)
# Window 3: [-5,-6,50,3] → sum = 42
# Max average = 51 / 4 = 12.75