class Solution(object):

    def maxStability(self, n, edges, k):

        parent = list(range(n))   # parent[i] = parent of node i (initially itself)
        size = [1] * n            # size of each component for union by size
        components = [n]          # number of connected components

        def find(x):
            if parent[x] != x:           # if x is not root
                parent[x] = find(parent[x])  # path compression
            return parent[x]             # return root parent

        def union(u,v):
            pu = find(u)   # root of u
            pv = find(v)   # root of v

            if pu == pv:   # already connected → cycle
                return False

            components[0] -= 1   # merging two components

            if size[pu] > size[pv]:   # attach smaller tree under bigger
                parent[pv] = pu
                size[pu] += size[pv]  # update size
            else:
                parent[pu] = pv
                size[pv] += size[pu]  # update size

            return True   # union successful

        must = []   # store mandatory edges
        flex = []   # store optional edges

        for e in edges:
            if e[3] == 1:       # mandatory edge
                must.append(e)
            else:               # optional edge
                flex.append(e)

        mini = float('inf')     # track minimum stability in final tree

        for u,v,w,t in must:
            mini = min(mini,w)  # mandatory edges limit stability
            if not union(u,v):  # cycle in mandatory edges
                return -1       # impossible to form tree

        flex.sort(key=lambda x: -x[2])  # sort optional edges by decreasing stability

        import heapq
        pq = []   # min heap to track used optional edges

        for u,v,w,t in flex:
            if union(u,v):          # add edge if it connects components
                heapq.heappush(pq,w) # store its stability

        while k > 0 and pq:         # apply upgrades while available
            x = heapq.heappop(pq)   # smallest stability edge
            mini = min(mini, 2*x)   # upgrading doubles its stability
            k -= 1                  # use one upgrade

        if components[0] != 1:      # graph not fully connected
            return -1

        if pq:                      # if edges remain in heap
            return min(mini, pq[0]) # min stability among all edges

        return mini                 # final stability of spanning tree