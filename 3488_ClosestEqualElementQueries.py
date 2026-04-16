class Solution(object):
    def solveQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        import bisect

        n = len(nums)
        nums_pos = defaultdict(list)

        # Store indices of each number
        for i in range(n):
            nums_pos[nums[i]].append(i)

        # Extend positions to handle circular distance
        for pos in nums_pos.values():
            x = pos[0]
            pos.insert(0, pos[-1] - n)
            pos.append(x + n)

        # Process each query
        for i in range(len(queries)):
            x = nums[queries[i]]
            pos_list = nums_pos[x]

            # If only one occurrence, no valid distance
            if len(pos_list) == 3:
                queries[i] = -1
                continue

            pos = bisect.bisect_left(pos_list, queries[i])

            # Find minimum distance to nearest same element
            queries[i] = min(
                pos_list[pos + 1] - pos_list[pos],
                pos_list[pos] - pos_list[pos - 1],
            )

        return queries