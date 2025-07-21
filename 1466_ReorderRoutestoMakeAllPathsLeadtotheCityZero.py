class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict, deque

        # Create an adjacency list to represent the graph
        # Each entry keeps (neighbor, needs_change) where needs_change is:
        # - 1 if the edge goes *away* from 0 (wrong direction)
        # - 0 if the edge goes *towards* 0 (correct direction)
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append((v, 1))  # Original direction (u -> v) might need to be changed
            graph[v].append((u, 0))  # Reverse direction (v -> u) is already correct

        visited = [False] * n       # Track visited cities
        queue = deque([0])          # Start BFS from city 0 (capital)
        count = 0                   # Count of edges that need to be reoriented

        # Perform BFS traversal
        while queue:
            city = queue.popleft()  # Get the current city
            visited[city] = True    # Mark it as visited

            for neighbor, needs_change in graph[city]:
                if not visited[neighbor]:
                    count += needs_change   # Add 1 if this edge needs to be changed
                    queue.append(neighbor)  # Visit the neighbor next

        return count  # Return the total number of changes required
