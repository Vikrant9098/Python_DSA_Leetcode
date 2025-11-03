class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [1] * n  # list to store super ugly numbers
        idx = [0] * len(primes)  # index pointers for each prime
        val = list(primes)  # current values for each prime

        for i in range(1, n):
            next_ugly = min(val)  # find smallest value among all primes
            ugly[i] = next_ugly  # store it as next super ugly number

            # update all primes that produced this number
            for j in range(len(primes)):
                if val[j] == next_ugly:
                    idx[j] += 1  # move index for that prime
                    val[j] = ugly[idx[j]] * primes[j]  # update next multiple value

        return ugly[-1]  # return nth super ugly number
