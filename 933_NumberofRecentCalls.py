from collections import deque

class RecentCounter(object):

    def __init__(self):
        """
        Initialize the RecentCounter object.
        Use a queue to store timestamps of recent requests.
        """
        self.queue = deque()  # double-ended queue for efficient popping from the front

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        Add the current timestamp t to the queue.
        Remove all timestamps that are older than t - 3000.
        Return the number of requests in the last 3000 milliseconds.
        """
        # Add the current ping time to the queue
        self.queue.append(t)

        # Remove all pings outside the [t - 3000, t] range
        while self.queue[0] < t - 3000:
            self.queue.popleft()  # Remove the oldest timestamp

        # The remaining elements are within the valid range
        return len(self.queue)
