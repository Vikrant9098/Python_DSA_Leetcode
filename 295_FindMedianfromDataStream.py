import heapq  # for min-heap implementation

class MedianFinder(object):

    def __init__(self):
        # Max-heap (simulated with negatives) for the smaller half of numbers
        self.max_heap = []
        # Min-heap for the larger half of numbers
        self.min_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # Push number into max_heap (as negative to simulate max-heap)
        heapq.heappush(self.max_heap, -num)
        # Balance: move largest from max_heap to min_heap
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # Ensure max_heap has equal or 1 more element than min_heap
        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self):
        """
        :rtype: float
        """
        # If odd, median = top of max_heap
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        # If even, median = average of tops of both heaps
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
