class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        """
        :type mountainHeight: int
        :type workerTimes: List[int]
        :rtype: int
        """
        
        lo, hi = 1, 10**16  # binary search range for minimum time

        while lo < hi:
            mid = (lo + hi) >> 1  # middle time to check
            tot = 0  # total height workers can reduce in 'mid' seconds

            for t in workerTimes:
                # compute max units this worker can reduce in 'mid' time
                # derived from k*(k+1)/2 * t <= mid
                tot += int(math.sqrt(mid / t * 2 + 0.25) - 0.5)

                if tot >= mountainHeight:  # stop early if enough work done
                    break

            if tot >= mountainHeight:
                hi = mid  # mid time works, try smaller time
            else:
                lo = mid + 1  # not enough work, increase time

        return lo  # minimum seconds needed