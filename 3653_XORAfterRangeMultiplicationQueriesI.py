class Solution:
    def xorAfterQueries(self, nums, queries):
        MOD = 10**9 + 7   # Large prime to prevent overflow during multiplication

        # Process each query one by one
        for l, r, k, v in queries:
            i = l   # start from index l
            
            # Traverse from l to r with step size k
            while i <= r:
                # Multiply current element by v and take modulo
                nums[i] = (nums[i] * v) % MOD
                
                # Move to next index with step k
                i += k

        ans = 0   # Initialize XOR result
        
        # Compute XOR of all elements in the updated array
        for num in nums:
            ans ^= num   # XOR accumulates values

        return ans   # Final XOR result