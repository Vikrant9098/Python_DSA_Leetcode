import heapq

class TaskManager(object):

    def __init__(self, tasks):
        """
        :type tasks: List[List[int]]
        """
        # Dictionary to store taskId -> (userId, priority)
        self.taskMap = {}

        # Heap (priority queue) to fetch the highest priority task
        # Store (-priority, -taskId, userId, taskId) to simulate max-heap
        self.pq = []

        # Initialize with given tasks
        for userId, taskId, priority in tasks:
            self.taskMap[taskId] = (userId, priority)
            heapq.heappush(self.pq, (-priority, -taskId, userId, taskId))

    def add(self, userId, taskId, priority):
        """
        :type userId: int
        :type taskId: int
        :type priority: int
        :rtype: None
        """
        self.taskMap[taskId] = (userId, priority)
        heapq.heappush(self.pq, (-priority, -taskId, userId, taskId))

    def edit(self, taskId, newPriority):
        """
        :type taskId: int
        :type newPriority: int
        :rtype: None
        """
        if taskId in self.taskMap:
            userId, _ = self.taskMap[taskId]
            # Update task with new priority
            self.taskMap[taskId] = (userId, newPriority)
            heapq.heappush(self.pq, (-newPriority, -taskId, userId, taskId))

    def rmv(self, taskId):
        """
        :type taskId: int
        :rtype: None
        """
        if taskId in self.taskMap:
            del self.taskMap[taskId]  # Lazy deletion (heap will skip later)

    def execTop(self):
        """
        :rtype: int
        """
        while self.pq:
            priority, negTaskId, userId, taskId = heapq.heappop(self.pq)
            if taskId in self.taskMap:
                curUser, curPriority = self.taskMap[taskId]
                # Validate that priority is still current
                if curPriority == -priority:
                    del self.taskMap[taskId]  # Remove executed task
                    return curUser
        return -1  # No tasks available
