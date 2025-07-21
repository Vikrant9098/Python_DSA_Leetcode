class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        from collections import defaultdict, deque

        # Graph will store the relationships between variables
        graph = defaultdict(list)

        # Build the graph from the equations and values
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))      # a / b = val → edge from a to b
            graph[b].append((a, 1.0 / val))  # b / a = 1/val → edge from b to a

        # Helper function to perform BFS from src to dest
        def bfs(src, dest):
            if src not in graph or dest not in graph:
                return -1.0  # If either variable is not in the graph

            queue = deque([(src, 1.0)])  # Start with src and initial product 1.0
            visited = set()  # To keep track of visited nodes

            while queue:
                node, prod = queue.popleft()

                if node == dest:
                    return prod  # Found destination, return the cumulative product

                visited.add(node)

                for neighbor, value in graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, prod * value))  # Multiply product with edge weight

            return -1.0  # Destination not reachable

        # Process each query using BFS
        result = []
        for a, b in queries:
            result.append(bfs(a, b))  # Evaluate each query using the graph

        return result
