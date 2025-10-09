import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        n = len(profits)  # number of projects
        projects = sorted(zip(capital, profits))  # sort projects by required capital
        max_heap = []  # max heap for profits (store negative to simulate max heap)
        i = 0  # pointer to go through sorted projects

        # choose at most k projects
        for _ in range(k):
            # add all projects we can afford with current capital
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])  # push negative profit
                i += 1
            
            # if no project can be started, stop
            if not max_heap:
                break
            
            # pick the project with max profit
            w += -heapq.heappop(max_heap)
        
        return w  # final maximized capital
