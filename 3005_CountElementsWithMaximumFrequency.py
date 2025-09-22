class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        
        # Count the frequency of each element
        freq = Counter(nums)
        
        # Find the maximum frequency
        max_freq = max(freq.values())
        
        # Count total elements having maximum frequency
        total = sum(count for count in freq.values() if count == max_freq)
        
        return total
