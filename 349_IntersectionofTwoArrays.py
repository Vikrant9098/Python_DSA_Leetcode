class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)        # convert nums1 to set to remove duplicates
        set2 = set(nums2)        # convert nums2 to set to remove duplicates

        result = set1 & set2     # find common elements using intersection operator

        return list(result)      # convert set to list and return
