class Solution(object):
    def maxPower(self, stations, r, k):
        """
        :type stations: List[int]
        :type r: int
        :type k: int
        :rtype: int
        """
        prefix = [0]  # prefix sum array to calculate range sums fast
        size = len(stations)  # total number of cities

        # build prefix sum of stations
        for i in stations:
            prefix.append(prefix[-1] + i)  # prefix[i+1] = sum of stations[0..i]

        # calculate total power for each city based on range r
        for i in range(size):
            stations[i] = prefix[min(i + r + 1, size)] - prefix[max(0, i - r)]
            # power[i] = sum of stations within range [i - r, i + r]

        # helper function to check if we can make all cities have at least 'min_power'
        def check(min_power):
            diff = [0] * size  # difference array for range updates
            cur_diff = 0  # current total extra power effect
            cnt_station = 0  # total new stations used so far

            for i, power in enumerate(stations):
                cur_diff += diff[i]  # apply ongoing additions to current city
                power_diff = min_power - power - cur_diff  # how much more power needed

                if power_diff > 0:  # if city power is less than required
                    cnt_station += power_diff  # add that many new stations
                    if cnt_station > k:  # if used more than allowed
                        return False  # cannot reach target
                    cur_diff += power_diff  # apply addition effect
                    if i + 2 * r + 1 < size:  # mark end of range effect
                        diff[i + 2 * r + 1] -= power_diff  # remove effect after range ends

            return True  # all cities reached at least min_power

        left = min(stations)  # minimum possible power
        right = left + k  # upper bound for binary search

        # binary search for maximum minimum power
        while left <= right:
            mid = left + (right - left) // 2  # guess a minimum power
            if check(mid):  # check if it's possible
                left = mid + 1  # try for higher value
            else:
                right = mid - 1  # try lower value

        return right  # maximum achievable minimum power
