class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # If there are no intervals, return an empty list
        if not intervals:
            return []

        # Sort intervals based on their start value
        intervals.sort(key=lambda x: x[0])

        # List to store the merged intervals
        result = []

        # Take the first interval as the current interval
        current = intervals[0]
        result.append(current)

        # Iterate through all intervals
        for interval in intervals:
            # Check if the current interval overlaps with the last one
            if interval[0] <= current[1]:
                # Merge by extending the end time with the maximum value
                current[1] = max(current[1], interval[1])
            else:
                # If no overlap, update current and add to result
                current = interval
                result.append(current)

        # Return the merged intervals
        return result
