class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # Step 1: Build graph as adjacency list
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)  
            # edge: pre -> course (to take "course" you must finish "pre")

        # Step 2: Create a visited array
        # 0 = unvisited, 1 = visiting, 2 = visited
        visited = [0] * numCourses

        # Step 3: DFS function to detect cycles
        def dfs(node):
            if visited[node] == 1:
                return False  # cycle detected
            if visited[node] == 2:
                return True   # already processed, no cycle here

            # mark current node as "visiting"
            visited[node] = 1

            # visit all neighbors
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            # mark as "visited"
            visited[node] = 2
            return True

        # Step 4: Run DFS for each course
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
