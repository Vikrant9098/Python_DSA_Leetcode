import heapq

class SmallestInfiniteSet(object):

    def __init__(self):
        # Min-heap to store added-back numbers
        self.min_heap = []
        # Set to avoid duplicates in heap
        self.added_back = set()
        # Smallest number not yet popped from the natural stream [1, 2, 3...]
        self.current = 1

    def popSmallest(self):
        """
        :rtype: int
        """
        # If there are any added-back smaller elements
        if self.min_heap:
            smallest = heapq.heappop(self.min_heap)  # Get smallest from heap
            self.added_back.remove(smallest)         # Remove from set
            return smallest
        else:
            # Return current smallest and move to next
            self.current += 1
            return self.current - 1

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        # Only add if number < current and not already present
        if num < self.current and num not in self.added_back:
            heapq.heappush(self.min_heap, num)  # Add to heap
            self.added_back.add(num)            # Track in set
