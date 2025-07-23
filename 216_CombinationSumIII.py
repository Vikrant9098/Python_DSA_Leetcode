class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        # Result list to store all valid combinations
        result = []

        # Helper function for backtracking
        def backtrack(start, path, remaining):
            """
            :param start: number to start from (to avoid reuse and ensure increasing order)
            :param path: current combination being built
            :param remaining: remaining sum to reach target n
            """
            # If the combination has k numbers and the remaining sum is 0, it's a valid answer
            if len(path) == k and remaining == 0:
                result.append(list(path))  # Add a copy of current path to result
                return

            # If combination is too long or sum exceeded, stop exploring
            if len(path) > k or remaining < 0:
                return

            # Try numbers from 'start' to 9
            for i in range(start, 10):
                # Add current number to path
                path.append(i)

                # Recurse with next number and reduced remaining sum
                backtrack(i + 1, path, remaining - i)

                # Backtrack: remove last added number and try next
                path.pop()

        # Start backtracking from number 1 with empty path and total sum n
        backtrack(1, [], n)

        return result
