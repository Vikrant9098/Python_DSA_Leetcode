class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """

        # Modulo value used to keep numbers within limits
        # and avoid integer overflow during matrix operations
        MOD = 10**9 + 7

        # Total distinct values available in the range [l, r]
        m = r - l + 1

        # If array length is 1, every value in the range
        # can form a valid array by itself
        if n == 1:
            return m

        def multiply(A, B):
            """
            Multiplies two m x m matrices A and B.
            Returns the resulting matrix modulo MOD.
            """

            # Initialize result matrix with zeros
            C = [[0] * m for _ in range(m)]

            # Standard matrix multiplication:
            # C[i][j] += A[i][k] * B[k][j]
            for i in range(m):
                for k in range(m):

                    # Skip unnecessary work if current element is 0
                    if A[i][k] == 0:
                        continue

                    for j in range(m):
                        C[i][j] = (
                            C[i][j]
                            + A[i][k] * B[k][j]
                        ) % MOD

            return C

        def fast_pow(A, p):
            """
            Computes A^p using Binary Exponentiation.
            Reduces complexity from O(p) multiplications
            to O(log p) multiplications.
            """

            # Create Identity Matrix
            # (Multiplicative identity for matrices)
            res = [[0] * m for _ in range(m)]
            for i in range(m):
                res[i][i] = 1

            while p > 0:

                # If current bit of exponent is 1,
                # multiply answer by current matrix
                if p % 2 == 1:
                    res = multiply(res, A)

                # Square the matrix for the next bit
                A = multiply(A, A)

                # Move to the next bit of exponent
                p //= 2

            return res

        # Transition Matrix
        #
        # T[i][j] = 1 means:
        # value j can come immediately after value i
        #
        # T[i][j] = 0 means:
        # transition is not allowed
        T = [[0] * m for _ in range(m)]

        for i in range(m):
            for j in range(m):

                # Valid transition condition
                #
                # Since values are mapped to indices:
                # actual values become:
                # value_i = l + i
                # value_j = l + j
                #
                # The condition for a valid zig-zag step
                # simplifies to:
                # i + j >= m
                if i + j >= m:
                    T[i][j] = 1

        # T^(n-1)
        #
        # In matrix exponentiation:
        # T^k stores the number of ways to move
        # from one state to another in exactly k steps.
        #
        # Since an array of length n contains
        # (n - 1) transitions, compute T^(n - 1).
        T_final = fast_pow(T, n - 1)

        # Sum all entries of T^(n-1)
        #
        # T_final[i][j] represents the number of valid
        # sequences that start at state i and end at state j.
        #
        # Summing all entries counts all valid sequences.
        total_sum = 0

        for i in range(m):
            total_sum = (total_sum + sum(T_final[i])) % MOD

        # Multiply by 2 because the matrix only counts
        # one direction of the zig-zag pattern.
        # The opposite direction contributes the same count.
        return (total_sum * 2) % MOD