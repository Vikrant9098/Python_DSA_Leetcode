class Solution(object):
    def smallestSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [0] * n

        # lastSeen[b] stores the last index where bit b (0 to 31) is seen
        lastSeen = [0] * 32

        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            # Update lastSeen for all bits that are set in nums[i]
            for b in range(32):
                if nums[i] & (1 << b):
                    lastSeen[b] = i

            # Find the farthest index needed to include all necessary bits
            maxEnd = i
            for b in range(32):
                maxEnd = max(maxEnd, lastSeen[b])

            # The length of the required subarray is (maxEnd - i + 1)
            answer[i] = maxEnd - i + 1

        return answer
