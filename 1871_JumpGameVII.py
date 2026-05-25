class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        
        n = len(s)

        # If last position is '1', we cannot reach the end
        if int(s[-1]):
            return False

        # dp[i] = True means index i is reachable
        dp = [False] * n
        dp[0] = True

        # reach stores count of reachable positions in current window
        # maxR stores maximum reachable index
        reach, maxR = 0, maxJump

        # Start checking from minJump index
        for i in range(minJump, n):

            # If current index is beyond maximum reachable range
            if i > maxR:
                return False

            # Add left side of sliding window
            reach += dp[i - minJump]

            # Remove out-of-window element
            if i > maxJump:
                reach -= dp[i - maxJump - 1]

            # Current index is reachable and value is '0'
            if reach and not int(s[i]):
                dp[i] = True
                maxR = i + maxJump

        return reach > 0