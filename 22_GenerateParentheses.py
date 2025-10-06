class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []  # List to store all valid parentheses combinations

        # Helper function for backtracking
        def backtrack(path, open_count, close_count):
            # If the current path has used all n pairs, add to result
            if len(path) == 2 * n:
                result.append("".join(path))  # Convert list to string and add
                return

            # Add an open parenthesis if we still have some left
            if open_count < n:
                path.append("(")  # Choose '('
                backtrack(path, open_count + 1, close_count)  # Recurse with incremented open_count
                path.pop()  # Undo the choice (backtrack)

            # Add a close parenthesis if it won't exceed open ones
            if close_count < open_count:
                path.append(")")  # Choose ')'
                backtrack(path, open_count, close_count + 1)  # Recurse with incremented close_count
                path.pop()  # Undo the choice (backtrack)

        # Start backtracking with empty path and zero open/close counts
        backtrack([], 0, 0)
        return result  # Return the final list of valid combinations
