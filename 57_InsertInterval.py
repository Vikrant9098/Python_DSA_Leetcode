class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # List to store the resulting merged intervals
        result = []

        i = 0
        n = len(intervals)

        # Add all intervals that end before the new interval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])  # No overlap, add as is
            i += 1

        # Merge all intervals that overlap with the new interval
        while i < n and intervals[i][0] <= newInterval[1]:
            # Update the start of newInterval to the minimum start
            newInterval[0] = min(newInterval[0], intervals[i][0])
            # Update the end of newInterval to the maximum end
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Add the merged new interval
        result.append(newInterval)

        # Add all remaining intervals after the new interval
        while i < n:
            result.append(intervals[i])
            i += 1

        # Return the final merged list of intervals
        return result
