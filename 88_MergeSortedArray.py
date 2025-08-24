class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # 'i' points to the last valid element in nums1 (index m-1)
        i = m - 1  

        # 'j' points to the last element in nums2 (index n-1)
        j = n - 1  

        # 'k' points to the last index of nums1 (size m+n-1),
        # where we will place the largest element at each step
        k = m + n - 1  

        # Merge while both arrays still have elements left to compare
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                # If nums1[i] is bigger, place it at nums1[k]
                nums1[k] = nums1[i]
                i -= 1
            else:
                # Otherwise, place nums2[j] at nums1[k]
                nums1[k] = nums2[j]
                j -= 1
            k -= 1  # Move the pointer for the next placement

        # If there are still elements left in nums2, copy them
        # (No need to handle leftover nums1, they’re already in place)
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
