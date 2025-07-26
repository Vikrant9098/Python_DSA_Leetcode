class Solution(object):
    def maxSubarrays(self, n, conflictingPairs):
        """
        :type n: int
        :type conflictingPairs: List[List[int]]
        :rtype: int
        """
        # Prepare buckets: for each L = min(a,b), store R = max(a,b)
        groups = [[] for _ in range(n+2)]
        for a, b in conflictingPairs:
            if a > b:
                a, b = b, a
            # Ignore any pair with R > n still safe (beyond array)
            groups[a].append(b)

        base = 0                  # Base count of valid subarrays when no removal
        gain = [0] * (n+2)        # Gain for removing conflict ending at R
        INF = n+1
        minR0, minR1 = INF, INF  # Placeholders for smallest and second-smallest R

        # Sweep from a = n down to 1
        for a in range(n, 0, -1):
            # Add all R where L == a
            for r in groups[a]:
                if r < minR0:
                    minR1 = minR0
                    minR0 = r
                elif r < minR1:
                    minR1 = r
            # All subarrays starting at a and ending before minR0 are valid
            base += (minR0 - a)
            # If we remove the conflict corresponding to minR0,
            # we can extend to minR1 instead—so gain is (minR1 - minR0)
            gain[minR0] += (minR1 - minR0)

        # Choose the best possible removal gain
        best_gain = max(gain)
        return base + best_gain
