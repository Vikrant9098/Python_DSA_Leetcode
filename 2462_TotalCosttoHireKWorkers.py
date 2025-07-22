import heapq

class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        
        n = len(costs)  # Total number of workers

        left_heap = []   # Min-heap for candidates from the left side
        right_heap = []  # Min-heap for candidates from the right side

        i, j = 0, n - 1  # Two pointers: i from start, j from end

        # Fill left_heap with first 'candidates' elements
        while i <= j and len(left_heap) < candidates:
            heapq.heappush(left_heap, costs[i])  # Push cost into left_heap
            i += 1  # Move the left pointer forward

        # Fill right_heap with last 'candidates' elements
        while j >= i and len(right_heap) < candidates:
            heapq.heappush(right_heap, costs[j])  # Push cost into right_heap
            j -= 1  # Move the right pointer backward

        total_cost = 0  # Initialize total cost

        for _ in range(k):  # We need to hire k workers
            # Case 1: Both heaps have elements
            if left_heap and right_heap:
                if left_heap[0] <= right_heap[0]:
                    total_cost += heapq.heappop(left_heap)  # Hire from left side
                    if i <= j:
                        heapq.heappush(left_heap, costs[i])  # Push next candidate to left_heap
                        i += 1
                else:
                    total_cost += heapq.heappop(right_heap)  # Hire from right side
                    if i <= j:
                        heapq.heappush(right_heap, costs[j])  # Push next candidate to right_heap
                        j -= 1

            # Case 2: Only left_heap has candidates
            elif left_heap:
                total_cost += heapq.heappop(left_heap)  # Hire from left
                if i <= j:
                    heapq.heappush(left_heap, costs[i])  # Add next to left_heap
                    i += 1

            # Case 3: Only right_heap has candidates
            else:
                total_cost += heapq.heappop(right_heap)  # Hire from right
                if i <= j:
                    heapq.heappush(right_heap, costs[j])  # Add next to right_heap
                    j -= 1

        return total_cost  # Return total cost after k hires
