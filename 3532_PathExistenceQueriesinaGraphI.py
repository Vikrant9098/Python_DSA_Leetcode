from typing import List


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        # comp[i] stores the connected component number of index i.
        # If two indices have the same component number,
        # then a path exists between them.
        comp = [0] * n

        # Traverse the sorted array from left to right.
        for i in range(1, n):

            # If the difference between adjacent elements is within maxDiff,
            # they belong to the same connected component.
            if nums[i] - nums[i - 1] <= maxDiff:
                comp[i] = comp[i - 1]

            # Otherwise, the gap is too large,
            # so start a new connected component.
            else:
                comp[i] = comp[i - 1] + 1

        # For each query (u, v):
        # If both indices belong to the same component,
        # a path exists; otherwise it does not.
        return [comp[u] == comp[v] for u, v in queries]