import heapq                           # Used for priority queue (min-heap)

class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):

        if len(source) != len(target): # If strings have different length, impossible
            return -1

        adj = [[] for _ in range(26)]   # Adjacency list for 26 lowercase letters

        for o, c, w in zip(original, changed, cost):
            # Convert characters to numbers (0–25) and store edge with cost
            adj[ord(o) - 97].append((ord(c) - 97, w))

        INF = 10**18                    # A very large value (represents infinity)

        dist = [[INF] * 26 for _ in range(26)]
        # dist[i][j] = minimum cost to convert char i → char j

        def dijkstra(src):
            pq = [(0, src)]             # Min-heap storing (cost, node)
            dist[src][src] = 0          # Cost to reach itself is 0

            while pq:
                d, u = heapq.heappop(pq)   # Get node with smallest cost

                if d > dist[src][u]:       # Skip outdated heap entry
                    continue

                for v, w in adj[u]:        # Visit all neighbors
                    if dist[src][v] > d + w:   # If cheaper path found
                        dist[src][v] = d + w   # Update minimum cost
                        heapq.heappush(pq, (dist[src][v], v))  # Push to heap

        for i in range(26):
            dijkstra(i)                 # Run Dijkstra from every character

        ans = 0                         # Stores total conversion cost

        for s, t in zip(source, target):
            u, v = ord(s) - 97, ord(t) - 97  # Convert characters to indices

            if u == v:                  # No cost if characters are same
                continue

            if dist[u][v] == INF:       # If conversion not possible
                return -1

            ans += dist[u][v]            # Add conversion cost

        return ans                       # Return total minimum cost
