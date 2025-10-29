from sortedcontainers import SortedList  # import SortedList for sorted window handling

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        window = SortedList()  # keeps last indexDiff numbers in sorted order
        
        # loop through all numbers
        for i in range(len(nums)):
            num = nums[i]  # current number
            
            # find the position to insert num - valueDiff
            pos = window.bisect_left(num - valueDiff)
            
            # check if there's a number within valueDiff range
            if pos < len(window) and abs(window[pos] - num) <= valueDiff:
                return True  # found valid pair
            
            window.add(num)  # add current number to window
            
            # keep only indexDiff elements in window
            if i >= indexDiff:
                window.remove(nums[i - indexDiff])  # remove old number
        
        return False  # no valid pair found
