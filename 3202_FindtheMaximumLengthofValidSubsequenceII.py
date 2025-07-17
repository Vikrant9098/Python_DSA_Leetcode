class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        
        # dp[i]: dict where key is modulo, value is max length of valid subsequence ending at i
        dp = [{} for _ in range(n)]
        
        max_len = 1  # single element is trivially a valid subsequence
        
        for i in range(n):
            dp[i] = {}
            for j in range(i):
                mod = (nums[j] + nums[i]) % k  # compute the pair's modulo

                # If nums[j] can end a valid subsequence with modulo 'mod'
                if mod in dp[j]:
                    dp[i][mod] = max(dp[i].get(mod, 0), dp[j][mod] + 1)
                else:
                    # Otherwise, start a new subsequence of length 2
                    dp[i][mod] = max(dp[i].get(mod, 0), 2)

                # Update the overall max length
                max_len = max(max_len, dp[i][mod])
        
        return max_len
