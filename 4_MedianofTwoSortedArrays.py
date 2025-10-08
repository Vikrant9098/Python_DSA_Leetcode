class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        # Binary search on the smaller array
        while left <= right:
            # Partition indices
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1

            # Edge cases: use +/- infinity if partition is at array boundary
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]

            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]

            # Check if correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # If total length is even
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                # If total length is odd
                else:
                    return max(maxLeft1, maxLeft2)
            # Move partition left
            elif maxLeft1 > minRight2:
                right = partition1 - 1
            # Move partition right
            else:
                left = partition1 + 1

        # If arrays are invalid
        raise ValueError("Input arrays are not sorted properly.")
