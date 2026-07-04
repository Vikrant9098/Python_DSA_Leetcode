from Queue import Queue          # Import Queue to perform BFS traversal
from sys import maxsize          # Import the largest possible integer value

class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int              # Number of cities
        :type roads: List[List[int]]   # Each road = [city1, city2, distance]
        :rtype: int               # Return the minimum score
        """

        ans = maxsize             # Store the minimum road distance found so far

        # Create an adjacency list with indices from 0 to n
        gr = [[] for _ in range(n + 1)]

        # Traverse every road in the input
        for edge in roads:

            # Add road from city1 -> city2 with its distance
            gr[edge[0]].append((edge[1], edge[2]))

            # Add road from city2 -> city1 (graph is undirected)
            gr[edge[1]].append((edge[0], edge[2]))

        # Create a visited array to avoid revisiting cities
        vis = [0] * (n + 1)

        # Create a queue for BFS
        q = Queue()

        # Start BFS from city 1
        q.put(1)

        # Mark city 1 as visited
        vis[1] = 1

        # Continue until the queue becomes empty
        while not q.empty():

            # Remove the front city from the queue
            node = q.get()

            # Traverse all neighbors of the current city
            for v, dis in gr[node]:

                # Update the answer with the smallest road distance seen
                ans = min(ans, dis)

                # If the neighboring city is not visited
                if vis[v] == 0:

                    # Mark it as visited
                    vis[v] = 1

                    # Add it to the queue for future processing
                    q.put(v)

        # Return the minimum road distance found in the connected component
        return ans