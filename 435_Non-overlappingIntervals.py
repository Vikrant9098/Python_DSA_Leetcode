class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) <= 1:
            return 0  # No need to remove anything if there's only 0 or 1 interval

        # Sort intervals by their end time (greedy approach)
        intervals.sort(key=lambda x: x[1])

        count = 0                 # Number of intervals to remove
        prev_end = intervals[0][1]  # End time of the last non-overlapping interval

        # Start checking from the second interval
        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < prev_end:
                # Current interval overlaps with previous -> remove it
                count += 1
            else:
                # No overlap, update previous end to current interval's end
                prev_end = end

        return count
