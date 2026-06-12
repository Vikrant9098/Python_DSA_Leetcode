class Solution:
    def dfs(self, node, par, d, adj):
        # Store depth of current node
        self.depth[node] = d

        # Store immediate parent (2^0-th ancestor)
        self.up[node][0] = par

        # Build binary lifting table for current node
        for j in range(1, self.log):

            # If previous ancestor does not exist
            if self.up[node][j - 1] == -1:
                self.up[node][j] = -1
            else:
                # 2^j-th ancestor = 2^(j-1)-th ancestor of
                # the 2^(j-1)-th ancestor
                self.up[node][j] = self.up[self.up[node][j - 1]][j - 1]

        # DFS on all children
        for child in adj[node]:

            # Skip parent node
            if child == par:
                continue

            # Visit child with increased depth
            self.dfs(child, node, d + 1, adj)

    def getLCA(self, u, v):
        # Make sure u is the deeper node
        if self.depth[u] < self.depth[v]:
            u, v = v, u

        # Lift u up until both nodes are at same depth
        for j in range(self.log - 1, -1, -1):
            if u != -1 and self.depth[u] - (1 << j) >= self.depth[v]:
                u = self.up[u][j]

        # If both nodes become same, that's the LCA
        if u == v:
            return u

        # Lift both nodes together while ancestors differ
        for j in range(self.log - 1, -1, -1):
            if self.up[u][j] != self.up[v][j]:
                u = self.up[u][j]
                v = self.up[v][j]

        # Parent of both nodes is the LCA
        return self.up[u][0]

    def assignEdgeWeights(self, edges, queries):
        n = len(edges) + 1
        MOD = 10**9 + 7

        # Number of levels needed for binary lifting
        self.log = n.bit_length()

        # Depth array for all nodes
        self.depth = [0] * (n + 1)

        # Binary lifting table
        self.up = [[-1] * self.log for _ in range(n + 1)]

        # Adjacency list representation of tree
        adj = [[] for _ in range(n + 1)]

        # Build undirected graph
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Preprocess depths and ancestors starting from root 1
        self.dfs(1, -1, 0, adj)

        # Precompute powers of 2 modulo MOD
        power = [1] * (n + 1)
        for i in range(1, n + 1):
            power[i] = (power[i - 1] * 2) % MOD

        # Store answers for queries
        ans = []

        # Process each query
        for u, v in queries:

            # Same node => path length is 0
            if u == v:
                ans.append(0)
                continue

            # Find Lowest Common Ancestor
            lca = self.getLCA(u, v)

            # Calculate distance between u and v
            length = self.depth[u] + self.depth[v] - 2 * self.depth[lca]

            # Answer = 2^(length - 1) mod MOD
            ans.append(power[length - 1])

        return ans