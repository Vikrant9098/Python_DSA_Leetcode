class Solution(object):
    def xorAfterQueries(self, nums, queries):
        """
        :type nums: List[int]          # Input array
        :type queries: List[List[int]] # Each query = [l, r, k, v]
        :rtype: int                   # Final XOR result
        """

        mod = 10**9 + 7               # Mod value to prevent overflow
        n = len(nums)                 # Size of array

        T = int(n**0.5)               # Threshold (sqrt decomposition)

        # groups[k] will store all queries having step size k (for small k)
        groups = [[] for _ in range(T)]
        
        # Step 1: Process queries
        for l, r, k, v in queries:
            if k < T:
                # Store small k queries for batch processing later
                groups[k].append((l, r, v))
            else:
                # Directly apply updates for large k (fewer elements affected)
                for i in range(l, r + 1, k):
                    nums[i] = nums[i] * v % mod

        # Difference array for multiplicative updates
        dif = [1] * (n + T)

        # Step 2: Handle small k queries using grouping
        for k in range(1, T):

            # Skip if no queries for this k
            if not groups[k]:
                continue

            # Reset difference array to 1 (neutral for multiplication)
            dif[:] = [1] * len(dif)

            # Apply range updates in difference array
            for l, r, v in groups[k]:
                dif[l] = dif[l] * v % mod   # Start multiplying from index l

                # Compute position after last valid index in this sequence
                R = ((r - l) // k + 1) * k + l

                # Use modular inverse to stop multiplication effect after R
                dif[R] = dif[R] * pow(v, mod - 2, mod) % mod

            # Build prefix multiplication with step k
            for i in range(k, n):
                dif[i] = dif[i] * dif[i - k] % mod

            # Apply accumulated multiplication to nums
            for i in range(n):
                nums[i] = nums[i] * dif[i] % mod

        res = 0  # Final XOR result
        
        # Step 3: Compute XOR of all elements
        for x in nums:
            res ^= x

        return res  # Return final answer