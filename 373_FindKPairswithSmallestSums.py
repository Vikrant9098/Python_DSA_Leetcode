import heapq  # import heapq for min-heap

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        result = []  # list to store the final pairs
        if not nums1 or not nums2 or k == 0:  # edge case check
            return result

        # min-heap to store [sum, index in nums1, index in nums2]
        min_heap = []

        # Initialize heap with first element of nums2 paired with up to first k elements of nums1
        for i in range(min(len(nums1), k)):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))  # push sum and indexes

        # Extract k smallest pairs
        while k > 0 and min_heap:
            sum_val, i, j = heapq.heappop(min_heap)  # get smallest sum pair
            result.append([nums1[i], nums2[j]])      # add actual pair to result
            k -= 1

            # If there is a next element in nums2 for current nums1[i], push new pair
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result  # return list of k smallest pairs
