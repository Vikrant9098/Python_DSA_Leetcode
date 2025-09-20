from collections import deque, defaultdict
import bisect

class Router(object):

    def __init__(self, memoryLimit):
        """
        :type memoryLimit: int
        """
        self.memoryLimit = memoryLimit              # store the max number of packets allowed
        self.queue = deque()                        # FIFO queue to store packets
        self.packet_set = set()                     # set to quickly check duplicates
        self.dest_map = defaultdict(list)           # map: destination -> sorted timestamps

    def addPacket(self, source, destination, timestamp):
        """
        :type source: int
        :type destination: int
        :type timestamp: int
        :rtype: bool
        """
        packet = (source, destination, timestamp)   # make a packet as a tuple

        if packet in self.packet_set:               # if packet already exists
            return False                            # not added, return False

        if len(self.queue) == self.memoryLimit:     # if memory is full
            old_source, old_dest, old_time = self.queue.popleft()  # remove oldest packet
            self.packet_set.remove((old_source, old_dest, old_time))  # also remove from set
            idx = bisect.bisect_left(self.dest_map[old_dest], old_time)  # find old timestamp
            if idx < len(self.dest_map[old_dest]) and self.dest_map[old_dest][idx] == old_time:
                self.dest_map[old_dest].pop(idx)    # remove timestamp from list

        self.queue.append(packet)                   # add packet to queue
        self.packet_set.add(packet)                 # add to set
        bisect.insort(self.dest_map[destination], timestamp)  # insert timestamp in sorted order

        return True                                 # packet successfully added

    def forwardPacket(self):
        """
        :rtype: List[int]
        """
        if not self.queue:                          # if no packet in queue
            return []                               # return empty list

        source, destination, timestamp = self.queue.popleft()  # get oldest packet
        self.packet_set.remove((source, destination, timestamp))  # remove from set

        idx = bisect.bisect_left(self.dest_map[destination], timestamp)  # find timestamp
        if idx < len(self.dest_map[destination]) and self.dest_map[destination][idx] == timestamp:
            self.dest_map[destination].pop(idx)     # remove timestamp from list

        return [source, destination, timestamp]     # return the packet

    def getCount(self, destination, startTime, endTime):
        """
        :type destination: int
        :type startTime: int
        :type endTime: int
        :rtype: int
        """
        timestamps = self.dest_map[destination]     # get timestamps list for destination
        left = bisect.bisect_left(timestamps, startTime)   # first index >= startTime
        right = bisect.bisect_right(timestamps, endTime)   # first index > endTime
        return right - left                         # number of timestamps in range
