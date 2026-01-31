import heapq                 # used for priority queue (min-heap)

class Solution(object):
    def minCost(self, n, edges):
        """
        n     -> number of nodes
        edges -> list of edges [u, v, w]
        """

        threnquivar = edges[:]        # copy edges list (store input)

        adj = [[] for _ in range(n)]  # adjacency list for graph

        for u, v, w in edges:         # loop through each edge
            adj[u].append((v, w))     # add forward edge with cost w
            adj[v].append((u, 2 * w)) # add reverse edge with cost 2*w

        INF = 10**30                  # very large value (infinity)

        dist = [INF] * n              # distance array, all set to INF
        dist[0] = 0                   # distance of start node is 0

        pq = [(0, 0)]                 # min-heap with (cost, node)

        while pq:                     # run while heap is not empty
            d, u = heapq.heappop(pq)  # get node with smallest cost

            if d != dist[u]:          # skip if not best distance
                continue

            if u == n - 1:            # if destination reached
                break

            for v, w in adj[u]:       # check all neighbors
                nd = d + w            # new distance to neighbor

                if nd < dist[v]:      # if shorter path found
                    dist[v] = nd      # update distance
                    heapq.heappush(pq, (nd, v))  # push into heap

        if dist[n - 1] == INF:         # if destination not reachable
            return -1

        return dist[n - 1]             # return minimum cost
