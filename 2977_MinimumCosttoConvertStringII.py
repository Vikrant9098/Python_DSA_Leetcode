class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """

        INF = 10**30                    # A very large value as infinite cost
        id = {}                         # Map each string to a unique ID
        lens = set()                    # Store lengths of original strings
        sz = 0                          # Count of unique strings

        dist = [[INF] * 201 for _ in range(201)]  # Distance matrix

        for s, t, c in zip(original, changed, cost):  # Loop through rules
            if s not in id:               # If source string not mapped
                id[s] = sz               # Assign new ID
                lens.add(len(s))         # Store its length
                sz += 1
            if t not in id:               # If target string not mapped
                id[t] = sz               # Assign new ID
                sz += 1
            dist[id[s]][id[t]] = min(dist[id[s]][id[t]], c)  # Store min cost

        for i in range(sz):               # Loop through all IDs
            dist[i][i] = 0               # Cost to convert to itself is zero

        for k in range(sz):               # Floyd–Warshall outer loop
            for i in range(sz):           # Middle loop
                if dist[i][k] < INF:      # If path i → k exists
                    for j in range(sz):   # Inner loop
                        if dist[k][j] < INF:  # If path k → j exists
                            dist[i][j] = min(
                                dist[i][j],
                                dist[i][k] + dist[k][j]
                            )

        n = len(source)                  # Length of source string
        dp = [INF] * (n + 1)             # dp[i] = min cost till index i
        dp[0] = 0                        # No cost for empty prefix

        for i in range(n):               # Traverse source string
            if dp[i] == INF:             # If unreachable
                continue

            if source[i] == target[i]:   # If characters match
                dp[i + 1] = min(dp[i + 1], dp[i])  # Move without cost

            for L in lens:               # Try all substring lengths
                if i + L > n:            # If out of bounds
                    continue
                s = source[i:i + L]      # Source substring
                t = target[i:i + L]      # Target substring
                if s in id and t in id:  # If both are mapped
                    dp[i + L] = min(
                        dp[i + L],
                        dp[i] + dist[id[s]][id[t]]
                    )

        return -1 if dp[n] == INF else dp[n]  # Return result
