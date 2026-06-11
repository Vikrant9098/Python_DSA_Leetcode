class Solution(object):
    MOD = 10**9 + 7

    def dfs(self, g, x, f):
        """
        :type g: List[List[int]]
        :type x: int
        :type f: int
        :rtype: int
        """

        # Store the maximum depth found among all child nodes
        max_dep = 0

        # Traverse all adjacent nodes
        for y in g[x]:

            # Skip the parent node to avoid revisiting it
            if y == f:
                continue

            # Update maximum depth from child subtrees
            max_dep = max(max_dep, self.dfs(g, y, x) + 1)

        # Return the maximum depth from current node
        return max_dep

    def assignEdgeWeights(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """

        # Number of nodes = number of edges + 1 (tree property)
        n = len(edges) + 1

        # Create adjacency list for the tree
        g = [[] for _ in range(n + 1)]

        # Build the undirected graph
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # Find the maximum depth of the tree starting from node 1
        max_dep = self.dfs(g, 1, 0)

        # Return 2^(max_depth - 1) modulo MOD
        return pow(2, max_dep - 1, self.MOD)