class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        from collections import deque

        # Step 1: Build graph (adjacency list) and indegree array
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Step 2: Fill graph and indegree
        for course, prereq in prerequisites:
            graph[prereq].append(course)   # prereq -> course
            indegree[course] += 1          # increase indegree of course

        # Step 3: Start with courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        order = []  # result order of courses

        # Step 4: Process courses in queue
        while queue:
            current = queue.popleft()
            order.append(current)

            # Reduce indegree of neighbors (courses depending on current)
            for neighbor in graph[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 5: Check if all courses are taken
        if len(order) == numCourses:
            return order
        else:
            return []
