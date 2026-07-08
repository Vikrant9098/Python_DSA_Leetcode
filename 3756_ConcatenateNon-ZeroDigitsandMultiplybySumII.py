MOD = 10**9 + 7

# Precompute powers of 10 modulo MOD.
# pow10[i] = (10^i) % MOD
pow10 = [1] * 100001
for i in range(1, 100001):
    pow10[i] = (pow10[i - 1] * 10) % MOD


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)

        # Prefix sum of all digits.
        # sum[i] = sum of digits from s[0] to s[i-1]
        sum = [0] * (n + 1)

        # Prefix number formed by concatenating only non-zero digits.
        # Example: "10230" -> x stores values for "123"
        x = [0] * (n + 1)

        # Prefix count of non-zero digits.
        cnt = [0] * (n + 1)

        # Build all prefix arrays.
        for i, c in enumerate(s):
            d = int(c)

            # Update prefix digit sum.
            sum[i + 1] = sum[i] + d

            # Append the digit only if it is non-zero.
            if d > 0:
                x[i + 1] = (x[i] * 10 + d) % MOD
            else:
                x[i + 1] = x[i]

            # Count non-zero digits.
            cnt[i + 1] = cnt[i] + (d > 0)

        m = len(queries)
        res = [0] * m

        # Process each query independently.
        for i in range(m):
            l = queries[i][0]
            r = queries[i][1] + 1  # Convert to exclusive right index.

            # Number of non-zero digits inside s[l:r].
            length = cnt[r] - cnt[l]

            # Extract the concatenated non-zero number of the substring.
            # Remove the prefix contribution using powers of 10.
            non_zero_number = (
                x[r] - x[l] * pow10[length]
            ) % MOD

            # Sum of all digits in the substring.
            digit_sum = sum[r] - sum[l]

            # Required answer = extracted number × digit sum.
            res[i] = (non_zero_number * digit_sum) % MOD

        return res