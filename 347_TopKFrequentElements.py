class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict

        freq_map = defaultdict(int)  # map to store frequency of each number
        for num in nums:
            freq_map[num] += 1  # count frequency

        # bucket array where index = frequency, each bucket holds list of numbers
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)  # put number in bucket corresponding to its frequency

        result = []
        # iterate from high frequency to low frequency
        for i in range(len(buckets) - 1, 0, -1):
            if buckets[i]:
                result.extend(buckets[i])  # add all numbers in this bucket
            if len(result) >= k:
                break  # stop when we have k elements

        return result[:k]  # return first k elements
