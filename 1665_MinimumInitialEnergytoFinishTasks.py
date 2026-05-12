class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        
        # Sort tasks based on (minimum required - actual cost)
        tasks.sort(key=lambda x: x[1] - x[0])

        ans = 0

        # Process each task
        for task in tasks:
            # Update minimum initial energy required
            ans = max(ans + task[0], task[1])

        return ans