class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        """
        :type nums: List[int]
        :type k: int
        :type numOperations: int
        :rtype: int
        """
        from collections import Counter  # Import Counter to count frequency
        from bisect import bisect_left, bisect_right  # Import for binary search
        import bisect

        count = Counter(nums)  # Count frequency of each number
        points = set()  # Set to store all important points

        for v in nums:  # Loop through all numbers
            points.add(v - k)  # Add left range
            points.add(v + k + 1)  # Add right range end
            points.add(v)  # Add actual value

        points = sorted(points)  # Sort all unique points
        diff = [0] * (len(points) + 1)  # Difference array for sweep line

        for v in nums:  # Loop through nums again
            L = bisect_left(points, v - k)  # Index of left boundary
            R = bisect_left(points, v + k + 1)  # Index of right boundary
            diff[L] += 1  # Start of interval adds 1
            diff[R] -= 1  # End of interval subtracts 1

        ans = 1  # Store max frequency
        s = 0  # Running sum for reachable elements

        for i, x in enumerate(points):  # Loop through all points
            s += diff[i]  # Update running sum
            cntX = count.get(x, 0)  # Count of elements already equal to x
            possible = min(s, cntX + numOperations)  # Max we can make equal to x
            ans = max(ans, possible)  # Update result if larger

        return ans  # Return final maximum frequency
