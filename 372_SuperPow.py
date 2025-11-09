class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        MOD = 1337  # given modulus value

        # helper function to calculate (x^n) % MOD
        def modPow(x, n):
            result = 1  # start result as 1
            x %= MOD     # keep x within MOD range
            for _ in range(n):  # repeat n times
                result = (result * x) % MOD  # multiply and take mod
            return result  # return final result

        # recursive function to handle large b
        def helper(a, b, index):
            if index < 0:  # base case: no digits left
                return 1
            lastDigit = b[index]  # get the last digit
            part1 = modPow(a, lastDigit)  # (a^lastDigit) % MOD
            part2 = modPow(helper(a, b, index - 1), 10)  # (previous_result^10) % MOD
            return (part1 * part2) % MOD  # combine both and take mod

        return helper(a % MOD, b, len(b) - 1)  # start recursion from last digit
