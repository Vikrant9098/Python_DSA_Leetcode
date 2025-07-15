class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        # Convert arrays to sets to handle duplicates and enable O(1) lookup
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Use set difference to find elements only in each array
        # set1 - set2: elements in nums1 but not in nums2
        # set2 - set1: elements in nums2 but not in nums1
        return [list(set1 - set2), list(set2 - set1)]