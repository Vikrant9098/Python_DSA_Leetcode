import heapq

class Solution(object):
    def minimumCost(self, nums, k, dist):
        """
        :type nums: List[int]
        :type k: int
        :type dist: int
        :rtype: int
        """

        # Length of the list
        n = len(nums)

        # To keep track of the minimum cost
        minCostSum = float("inf")

        # Max heap to store the (k-2) smallest elements on the right
        # Stored as (-value, -index, index) to simulate max heap
        maxHeap = []

        # Sum of selected (k - 2) smallest values
        minRightSum = 0

        # Set to track indices currently included in maxHeap
        indices = set()

        # Min heap to store extra candidates that may be useful later
        minHeap = []

        # Initial window: pick elements from index 2 to dist + 1
        for i in range(2, min(dist + 2, n)):

            heapq.heappush(maxHeap, [-nums[i], -i, i])
            minRightSum += nums[i]
            indices.add(i)

            # Keep only (k - 2) smallest elements
            if len(indices) > k - 2:
                val, _, idx = heapq.heappop(maxHeap)

                # Push removed element into minHeap
                heapq.heappush(minHeap, [-val, idx, idx])

                minRightSum -= -val
                indices.remove(idx)

        # Sliding window starts from index 1
        for i in range(1, n - (k - 2)):

            # Remove invalid elements from heaps
            while maxHeap and maxHeap[0][2] not in indices:
                heapq.heappop(maxHeap)

            while minHeap and minHeap[0][2] <= i:
                heapq.heappop(minHeap)

            # Update minimum cost
            minCostSum = min(minCostSum, nums[0] + nums[i] + minRightSum)

            # If element leaving window is part of selected indices
            if i + 1 in indices:

                minRightSum -= nums[i + 1]
                indices.remove(i + 1)

                # Replace it with best available candidate
                if minHeap:
                    top = heapq.heappop(minHeap)
                    heapq.heappush(maxHeap, [-top[0], -top[2], top[2]])

                    indices.add(top[2])
                    minRightSum += top[0]

            # Add new element entering the window
            if i + 1 + dist < n:

                heapq.heappush(
                    maxHeap,
                    [-nums[i + 1 + dist], -(i + 1 + dist), i + 1 + dist]
                )

                minRightSum += nums[i + 1 + dist]
                indices.add(i + 1 + dist)

                # Maintain size constraint
                if len(indices) > k - 2:
                    val, _, idx = heapq.heappop(maxHeap)

                    heapq.heappush(minHeap, [-val, idx, idx])
                    minRightSum -= -val

                    if idx in indices:
                        indices.remove(idx)

        return minCostSum
