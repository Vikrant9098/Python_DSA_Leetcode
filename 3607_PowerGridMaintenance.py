class Solution(object):
    def processQueries(self, c, connections, queries):
        """
        :type c: int
        :type connections: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        from collections import defaultdict, deque
        import bisect

        # create graph as adjacency list
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)      # add edge u to v
            graph[v].append(u)      # add edge v to u

        # store component id for each station
        comp = [0] * (c + 1)
        comp_id = 0                # start component counter

        # find connected components using BFS
        for i in range(1, c + 1):
            if comp[i] == 0:       # if not yet visited
                comp_id += 1       # new component id
                queue = deque([i]) # start BFS
                comp[i] = comp_id
                while queue:
                    node = queue.popleft()     # take current node
                    for nei in graph[node]:    # visit neighbors
                        if comp[nei] == 0:     # if not visited
                            comp[nei] = comp_id
                            queue.append(nei)

        # map: component id -> sorted list of online stations
        comp_online = defaultdict(list)
        for i in range(1, c + 1):
            cid = comp[i]
            bisect.insort(comp_online[cid], i)  # keep list sorted

        # all stations start online
        online = [True] * (c + 1)

        # list to store answers
        result = []

        # process each query
        for qtype, x in queries:
            if qtype == 1:                     # maintenance check
                if online[x]:                  # if station is online
                    result.append(x)
                else:
                    cid = comp[x]              # find its component
                    arr = comp_online[cid]     # online stations in it
                    if not arr:                # if none online
                        result.append(-1)
                    else:
                        result.append(arr[0])  # smallest online station id
            else:                              # goes offline
                if online[x]:                  # if it's online
                    online[x] = False          # mark offline
                    cid = comp[x]              # get its component
                    arr = comp_online[cid]
                    idx = bisect.bisect_left(arr, x)  # find index
                    if idx < len(arr) and arr[idx] == x:
                        arr.pop(idx)           # remove from list

        return result                          # return final output
