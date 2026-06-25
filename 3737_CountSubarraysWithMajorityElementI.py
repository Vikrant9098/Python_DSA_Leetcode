class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # Length of the input array
        n = len(nums)

        # Stores the total number of valid subarrays
        ans = 0

        # Choose the starting index of the subarray
        for l in range(n):

            # Count of target elements in the current subarray
            target_count = 0

            # Extend the subarray from index l to n - 1
            for r in range(l, n):

                # Increment target count if current element equals target
                if nums[r] == target:
                    target_count += 1

                # Current subarray length
                length = r - l + 1

                # A target is a majority element if it appears
                # more than half of the subarray length
                if target_count > length // 2:
                    ans += 1

        # Return the total count of majority subarrays
        return ans