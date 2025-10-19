class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        from collections import deque  # import deque for queue operations

        queue = deque([s])  # create a queue and put the initial string in it
        visited = set([s])  # create a set to keep track of visited strings
        smallest = s         # store the smallest string found so far

        while queue:  # loop until the queue is empty
            curr = queue.popleft()  # take the first string from the queue

            if curr < smallest:  # if the current string is smaller lexicographically
                smallest = curr  # update the smallest string

            # ---- Operation 1: Add 'a' to all odd indices ----
            chars = list(curr)  # convert string to list for easy modification
            for i in range(1, len(chars), 2):  # loop through all odd indices
                new_digit = (int(chars[i]) + a) % 10  # add 'a' to the digit and wrap around 10
                chars[i] = str(new_digit)  # convert the new digit back to a string
            added = "".join(chars)  # join the list back into a string

            if added not in visited:  # if this string was not seen before
                visited.add(added)  # mark it as visited
                queue.append(added)  # add it to the queue to explore later

            # ---- Operation 2: Rotate string to the right by 'b' ----
            rotated = curr[-b:] + curr[:-b]  # take last 'b' chars and move them to front

            if rotated not in visited:  # if rotated string is new
                visited.add(rotated)  # mark it as visited
                queue.append(rotated)  # add it to the queue

        return smallest  # return the lexicographically smallest string found
