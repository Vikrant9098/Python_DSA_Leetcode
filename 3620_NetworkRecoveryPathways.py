class Solution:
    def check(self, mid, adj, topo, online, k, n):

        # dist[i] = minimum total path cost to reach node i
        dist = [inf] * n
        dist[0] = 0  # Start from node 0

        # Process nodes in topological order (graph is a DAG)
        for u in topo:

            # Skip if node is unreachable
            if dist[u] == inf:
                continue

            # Ignore offline intermediate nodes
            # (source and destination are always allowed)
            if u != 0 and u != n - 1 and not online[u]:
                continue

            # Explore all outgoing edges
            for v, w in adj[u]:

                # Ignore edges whose score is smaller than current threshold
                if w < mid:
                    continue

                # Cannot move to an offline intermediate node
                if v != n - 1 and not online[v]:
                    continue

                # Relax the edge with minimum path cost
                dist[v] = min(dist[v], dist[u] + w)

        # Valid only if destination can be reached within cost k
        return dist[n - 1] <= k

    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        # Build adjacency list
        adj = [[] for _ in range(n)]
        indegree = [0] * n

        max_edge = 0  # Largest edge weight for binary search

        for u, v, w in edges:
            adj[u].append((v, w))
            indegree[v] += 1
            max_edge = max(max_edge, w)

        q = deque()

        # Start Kahn's algorithm with nodes having indegree 0
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        topo = []

        # Generate topological ordering of the DAG
        while q:
            u = q.popleft()
            topo.append(u)

            for v, _ in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        # Binary search on the minimum edge score allowed in the path
        low, high = 0, max_edge
        ans = -1

        while low <= high:

            # Candidate minimum edge weight
            mid = (low + high) // 2

            # If a valid path exists with every edge >= mid
            if self.check(mid, adj, topo, online, k, n):
                ans = mid          # Try to increase the minimum edge score
                low = mid + 1
            else:
                high = mid - 1     # Threshold too high, decrease it

        # Maximum possible minimum edge score
        return ans