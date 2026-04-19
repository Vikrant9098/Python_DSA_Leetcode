class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
        # Initialize two pointers for nums1 and nums2
        i = 0  # pointer for nums1
        j = 0  # pointer for nums2
        
        # Traverse both arrays while pointers are within bounds
        while i < len(nums1) and j < len(nums2):
            
            # If nums1[i] > nums2[j], it means this pair is invalid
            # So we move i forward to find a smaller value in nums1
            # (True = 1, False = 0, so this line conditionally increments i)
            i += nums1[i] > nums2[j]
            
            # Always move j forward to explore more pairs
            j += 1
        
        # j has moved one step ahead in the last iteration
        # So the valid distance is (j - i - 1)
        # max(0, ...) ensures we don't return negative values
        return max(0, j - i - 1)