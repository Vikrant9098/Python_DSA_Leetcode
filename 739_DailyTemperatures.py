class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)              # Total number of days
        answer = [0] * n                   # Initialize answer list with 0s
        stack = []                         # Stack to store indices

        # Iterate from the end of the list to the beginning
        for i in range(n - 1, -1, -1):
            current_temp = temperatures[i]

            # Pop elements from the stack while current temp >= temp at top of stack
            while stack and temperatures[stack[-1]] <= current_temp:
                stack.pop()

            # If stack is not empty, top of stack is the next warmer day
            if stack:
                answer[i] = stack[-1] - i  # Calculate the number of days to wait

            # Push current index onto the stack
            stack.append(i)

        return answer
