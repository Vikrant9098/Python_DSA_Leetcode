import heapq  # import heapq for priority queue operations

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        points = []  # list to store all building start and end points
        
        # loop through each building
        for left, right, height in buildings:
            points.append((left, -height))  # add start point (negative height)
            points.append((right, height))  # add end point (positive height)
        
        points.sort()  # sort all points by x coordinate and height
        
        heap = [0]  # initialize heap with ground level (0)
        prev_height = 0  # store previous maximum height
        result = []  # store final skyline points
        active = {0: 1}  # dictionary to count active heights
        
        # go through each point in sorted order
        for x, h in points:
            if h < 0:  # if it's a start point
                heapq.heappush(heap, h)  # push height into heap (negative for max-heap)
                active[-h] = active.get(-h, 0) + 1  # increase count of this height
            else:  # if it's an end point
                active[h] -= 1  # decrease count of this height
                if active[h] == 0:  # if count becomes zero
                    del active[h]  # remove height from active dictionary
            
            # remove heights from heap that are no longer active
            while -heap[0] not in active:
                heapq.heappop(heap)
            
            curr_height = -heap[0]  # current tallest building height
            
            # if skyline height changes, record this point
            if curr_height != prev_height:
                result.append([x, curr_height])  # add key point
                prev_height = curr_height  # update previous height
        
        return result  # return final skyline list
