class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # if only one node, return it
        if n == 1:
            return [0]
        
        # build adjacency list (graph)
        graph = [set() for _ in range(n)]
        for a, b in edges:
            graph[a].add(b)  # connect a to b
            graph[b].add(a)  # connect b to a (undirected)
        
        # find initial leaves (nodes with 1 neighbor)
        leaves = [i for i in range(n) if len(graph[i]) == 1]
        
        # remove leaves layer by layer until 1 or 2 nodes remain
        while n > 2:
            n -= len(leaves)  # reduce node count
            new_leaves = []   # store next round of leaves
            
            for leaf in leaves:
                neighbor = graph[leaf].pop()   # get the connected node
                graph[neighbor].remove(leaf)   # remove leaf from neighbor
                if len(graph[neighbor]) == 1:  # if neighbor becomes a leaf
                    new_leaves.append(neighbor)
            
            leaves = new_leaves  # update leaves list
        
        # remaining nodes are MHT roots
        return leaves
