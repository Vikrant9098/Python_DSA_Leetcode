import heapq  # Import heapq module for using heap operations

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Create a min-heap with the first k elements
        min_heap = nums[:k]
        heapq.heapify(min_heap)  # Heapify to maintain the heap property

        # Iterate through the rest of the numbers
        for num in nums[k:]:
            if num > min_heap[0]:        # If current num is bigger than heap root
                heapq.heappop(min_heap)  # Remove the smallest in heap
                heapq.heappush(min_heap, num)  # Push the current num to maintain size k

        return min_heap[0]  # The root of the heap is the kth largest element
