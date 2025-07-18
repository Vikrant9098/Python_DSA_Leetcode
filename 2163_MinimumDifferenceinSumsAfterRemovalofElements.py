import heapq  # Import heap functions (min-heap by default)

class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums) // 3  # Total elements to remove is n
        length = len(nums)  # Total length is 3n

        # Array to store prefix sums (left side) of smallest n elements
        left_sum = [0] * length
        max_heap = []        # Max heap to track smallest n elements (simulated using negatives)
        left_total = 0       # Running total of smallest n elements from the left

        # Traverse from left to right
        for i in range(length):
            heapq.heappush(max_heap, -nums[i])  # Push negative to simulate max-heap
            left_total += nums[i]               # Add current element to total

            # If heap has more than n elements, remove largest (which is smallest negative)
            if len(max_heap) > n:
                left_total += heapq.heappop(max_heap)  # Add back (since it was negative)

            # When we have exactly n elements, store the sum at index i
            if len(max_heap) == n:
                left_sum[i] = left_total

        # Array to store suffix sums (right side) of largest n elements
        right_sum = [0] * length
        min_heap = []        # Min heap to track largest n elements from the right
        right_total = 0      # Running total of largest n elements from the right

        # Traverse from right to left
        for i in range(length - 1, -1, -1):
            heapq.heappush(min_heap, nums[i])  # Push normally (min-heap)
            right_total += nums[i]             # Add current element to total

            # If heap has more than n elements, remove smallest
            if len(min_heap) > n:
                right_total -= heapq.heappop(min_heap)  # Subtract the removed element

            # When we have exactly n elements, store the sum at index i
            if len(min_heap) == n:
                right_sum[i] = right_total

        # Initialize result to a large value (we'll minimize this)
        result = float('inf')

        # Try every possible split point between left and right parts
        for i in range(n - 1, 2 * n):
            # Calculate difference and update minimum result
            result = min(result, left_sum[i] - right_sum[i + 1])

        return result  # Return the minimum difference found
