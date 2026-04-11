class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nxt = [-1] * n        # stores next occurrence index for each position
        occur = {}            # map: value -> latest index (from right)
        ans = n + 1           # initialize with large value

        # build next occurrence array
        for i in range(n - 1, -1, -1):
            if nums[i] in occur:
                nxt[i] = occur[nums[i]]   # next same element index
            occur[nums[i]] = i            # update latest index

        # check triples (i, j, k) of same value
        for i in range(n):
            second_pos = nxt[i]           # second occurrence
            if second_pos != -1:
                third_pos = nxt[second_pos]  # third occurrence
                if third_pos != -1:
                    ans = min(ans, third_pos - i)  # minimize span

        return -1 if ans == n + 1 else ans * 2  # return result