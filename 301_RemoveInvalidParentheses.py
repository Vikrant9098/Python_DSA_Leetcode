from collections import deque  # import deque for BFS queue

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []  # list to store valid results
        if not s:
            return [""]  # if string is empty, return list with empty string

        visited = set()  # to keep track of visited strings
        queue = deque([s])  # start BFS with given string
        visited.add(s)  # mark starting string as visited
        found = False  # flag to stop after first valid level

        while queue:  # while there are strings to check
            curr = queue.popleft()  # remove first string from queue

            if self.isValid(curr):  # check if current string is valid
                res.append(curr)  # add valid string to result list
                found = True  # mark that valid string is found

            if found:
                continue  # skip generating next level once valid found

            for i in range(len(curr)):  # try removing one char at a time
                if curr[i] not in ('(', ')'):  # skip non-parenthesis chars
                    continue

                next_str = curr[:i] + curr[i + 1:]  # remove char at index i

                if next_str not in visited:  # if not already checked
                    visited.add(next_str)  # mark as visited
                    queue.append(next_str)  # add to queue for checking

        return res  # return all valid strings found

    def isValid(self, s):
        """Helper function to check if parentheses are balanced"""
        count = 0  # counter for balance
        for c in s:  # loop through each char
            if c == '(':
                count += 1  # increase for opening bracket
            elif c == ')':
                count -= 1  # decrease for closing bracket
            if count < 0:  # more closing brackets
                return False  # invalid string
        return count == 0  # valid only if all opened are closed
