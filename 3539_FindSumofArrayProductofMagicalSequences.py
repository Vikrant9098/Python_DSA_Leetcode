class Solution(object):
    def magicalSum(self, m, k, nums):
        """
        :type m: int
        :type k: int
        :type nums: List[int]
        :rtype: int
        """
        M = 10**9 + 7  # Mod value to prevent overflow
        l = len(nums)  # Length of nums array
        d = {}  # Memoization dictionary to store results

        # Recursive helper function
        def f(r, n, i, c):
            # Base cases to stop recursion if invalid
            if r < 0 or n < 0 or r + bin(c).count('1') < n:
                return 0
            # If no more elements to pick
            if r == 0:
                return 1 if n == bin(c).count('1') else 0
            # If reached end of nums
            if i >= l:
                return 0

            # Create a key to remember current state
            key = (r, n, i, c)
            if key in d:  # Return cached result if already computed
                return d[key]

            res = 0  # Initialize result for this state

            # Try picking t elements from current index
            for t in range(r + 1):
                w = 1  # Combination coefficient
                for j in range(t):  # Calculate nCr (r choose t)
                    w = w * (r - j) // (j + 1)
                w %= M  # Apply modulo

                v = pow(nums[i], t, M)  # nums[i]^t % M
                nc = c + t  # Update count for binary representation
                # Recursive call for next index and reduced size
                res = (res + w * v % M * f(r - t, n - (nc % 2), i + 1, nc // 2)) % M

            d[key] = res  # Store result in memoization dictionary
            return res  # Return result for current state

        # Start recursion with full values
        return f(m, k, 0, 0)
