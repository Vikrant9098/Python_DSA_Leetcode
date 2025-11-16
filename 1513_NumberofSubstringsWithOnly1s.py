class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 1000000007     # modulo value
        count = 0            # count of consecutive '1's
        ans = 0              # final answer

        for c in s:          # loop through each character
            if c == '1':     # if current char is '1'
                count += 1   # increase consecutive count
                ans = (ans + count) % MOD  # add new substrings
            else:
                count = 0    # reset when '0' comes

        return ans           # return answer
