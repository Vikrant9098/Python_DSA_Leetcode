class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        # Store all elements of nums1 in a set for fast lookup
        set1 = set(nums1)

        # Traverse nums2 and check whether element exists in set1
        for num in nums2:

            # If common element is found, return it immediately
            if num in set1:
                return num

        # If no common element exists, return -1
        return -1