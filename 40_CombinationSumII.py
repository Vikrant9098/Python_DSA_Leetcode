class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Sort candidates to handle duplicates easily
        candidates.sort()

        # Result list to store all unique combinations
        result = []

        # Helper function for backtracking
        def backtrack(temp_list, remain, start):
            # If remaining target is zero, add current combination to result
            if remain == 0:
                result.append(list(temp_list))
                return

            # Loop through candidates starting from index 'start'
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # If current number exceeds remaining target, stop
                if candidates[i] > remain:
                    break

                # Choose current number
                temp_list.append(candidates[i])

                # Recurse with reduced target and next index (i+1, use once)
                backtrack(temp_list, remain - candidates[i], i + 1)

                # Backtrack: remove last chosen number
                temp_list.pop()

        # Start backtracking with empty list, full target, starting at index 0
        backtrack([], target, 0)

        # Return final result
        return result
