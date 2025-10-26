class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 2:
            return 0  # Less than 2 elements → max gap = 0

        n = len(nums)
        min_val, max_val = min(nums), max(nums)  # Find global min and max

        if min_val == max_val:
            return 0  # All numbers are the same → max gap = 0

        # Calculate bucket size (at least 1) and total number of buckets
        bucket_size = max(1, (max_val - min_val) // (n - 1))  # Minimum possible gap
        bucket_count = (max_val - min_val) // bucket_size + 1  # Number of buckets

        # Initialize buckets for min and max values
        bucket_min = [float('inf')] * bucket_count  # Min value in each bucket
        bucket_max = [float('-inf')] * bucket_count  # Max value in each bucket

        # Put numbers into corresponding buckets
        for num in nums:
            idx = (num - min_val) // bucket_size  # Determine bucket index
            bucket_min[idx] = min(bucket_min[idx], num)  # Update bucket min
            bucket_max[idx] = max(bucket_max[idx], num)  # Update bucket max

        # Compute maximum gap between consecutive non-empty buckets
        max_gap = 0
        previous = min_val  # Track previous bucket's max
        for i in range(bucket_count):
            if bucket_min[i] == float('inf'):
                continue  # Skip empty buckets
            max_gap = max(max_gap, bucket_min[i] - previous)  # Gap between buckets
            previous = bucket_max[i]  # Update previous for next iteration

        return max_gap  # Return the maximum gap
