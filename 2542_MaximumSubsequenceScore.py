import heapq

class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """

        # Zip both arrays together as pairs (nums2[i], nums1[i]) for sorting
        pairs = zip(nums2, nums1)

        # Sort pairs in descending order based on nums2[i] because we want larger minimum later
        pairs = sorted(pairs, reverse=True)

        min_heap = []  # Min-heap to store top k nums1 values
        curr_sum = 0   # Current sum of nums1 values in the heap
        max_score = 0  # Variable to track the maximum score

        for num2, num1 in pairs:
            # Add current nums1 value to the sum
            curr_sum += num1
            # Push it into min-heap
            heapq.heappush(min_heap, num1)

            # If heap exceeds size k, remove the smallest element
            if len(min_heap) > k:
                curr_sum -= heapq.heappop(min_heap)

            # When heap has exactly k elements, calculate score
            if len(min_heap) == k:
                score = curr_sum * num2   # current sum of nums1 * current nums2 (as min among selected)
                max_score = max(max_score, score)  # update max score if better

        return max_score  # Return the best score found
