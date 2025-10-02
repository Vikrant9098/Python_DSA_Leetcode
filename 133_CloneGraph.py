# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        # If the input graph is empty, return None
        if not node:
            return None

        # A dictionary to store mapping: original node -> cloned node
        visited = {}

        # Helper function to clone using DFS
        def dfs(current):
            # If this node is already cloned, return the clone
            if current in visited:
                return visited[current]

            # Create a new clone node with the same value
            clone = Node(current.val)

            # Store the clone in visited dictionary
            visited[current] = clone

            # Go through all neighbors of the current node
            for neighbor in current.neighbors:
                # Recursively clone the neighbor and add it to the clone's neighbors list
                clone.neighbors.append(dfs(neighbor))

            # Return the fully cloned node
            return clone

        # Start DFS from the given node
        return dfs(node)
