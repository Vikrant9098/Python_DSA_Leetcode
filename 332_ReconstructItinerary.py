class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        import heapq

        graph = defaultdict(list)  # map each airport to its destinations

        # build the graph
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)  # push destination in min-heap (sorted order)

        route = []  # list to store final route

        def dfs(airport):
            heap = graph[airport]  # get all destinations from this airport
            while heap:  # visit all destinations
                next_airport = heapq.heappop(heap)  # get smallest (lexical) destination
                dfs(next_airport)  # visit next airport
            route.append(airport)  # add airport after visiting all paths

        dfs("JFK")  # start DFS from JFK
        return route[::-1]  # reverse route to get correct order
