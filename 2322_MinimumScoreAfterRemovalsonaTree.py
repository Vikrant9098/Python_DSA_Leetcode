class Solution(object):  # define the class Solution
    def minimumScore(self, nums, edges):  # main function taking node values and edges
        from collections import defaultdict  # import defaultdict for adjacency list

        n = len(nums)  # total number of nodes

        tree = defaultdict(list)  # create adjacency list for the tree

        for u, v in edges:  # loop through each edge
            tree[u].append(v)  # add v to u's adjacency list
            tree[v].append(u)  # add u to v's adjacency list (undirected)

        xor = [0] * n  # array to store XOR of subtree rooted at each node
        in_time = [0] * n  # array to store DFS entry time for each node
        out_time = [0] * n  # array to store DFS exit time for each node
        time = [0]  # mutable time counter used in DFS

        def dfs(node, parent):  # DFS function to compute subtree XOR and in/out times
            xor[node] = nums[node]  # initialize XOR with current node's value
            time[0] += 1  # increment global time
            in_time[node] = time[0]  # set in-time for the current node

            for nei in tree[node]:  # explore all connected nodes (neighbors)
                if nei != parent:  # skip parent to avoid revisiting
                    dfs(nei, node)  # recursively run DFS for child node
                    xor[node] ^= xor[nei]  # update XOR for current node's subtree

            time[0] += 1  # increment time after visiting children
            out_time[node] = time[0]  # set out-time for current node

        dfs(0, -1)  # run DFS from root node (0), parent is -1 (no parent)

        nodes = list(range(1, n))  # prepare list of nodes excluding root (0)

        min_score = float('inf')  # initialize result as infinity

        def is_ancestor(u, v):  # function to check if u is ancestor of v
            return in_time[u] <= in_time[v] and out_time[v] <= out_time[u]

        for i in range(len(nodes)):  # iterate over all nodes for first cut
            for j in range(i + 1, len(nodes)):  # iterate over remaining nodes for second cut
                a = nodes[i]  # first cut node
                b = nodes[j]  # second cut node

                if is_ancestor(a, b):  # if a is ancestor of b
                    x1 = xor[b]  # subtree rooted at b
                    x2 = xor[a] ^ xor[b]  # rest of a’s subtree
                    x3 = xor[0] ^ xor[a]  # rest of the tree
                elif is_ancestor(b, a):  # if b is ancestor of a
                    x1 = xor[a]  # subtree rooted at a
                    x2 = xor[b] ^ xor[a]  # rest of b’s subtree
                    x3 = xor[0] ^ xor[b]  # rest of the tree
                else:  # if a and b are in separate subtrees
                    x1 = xor[a]  # subtree rooted at a
                    x2 = xor[b]  # subtree rooted at b
                    x3 = xor[0] ^ xor[a] ^ xor[b]  # rest of the tree

                max_x = max(x1, x2, x3)  # find max XOR among 3 parts
                min_x = min(x1, x2, x3)  # find min XOR among 3 parts
                min_score = min(min_score, max_x - min_x)  # update minimum score

        return min_score  # return the final minimum score
