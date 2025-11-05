class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        res = []                                # final result list to store each window's x-sum

        counts = defaultdict(int)               # frequency map of numbers

        # count frequencies for the first window of size k
        for i in range(k):
            counts[nums[i]] += 1

        low = []                                # min-heap for elements not in top x

        # fill heap with (-count, -num) for sorting by freq then value (max-heap behavior)
        for n, c in counts.items():
            heapq.heappush(low, (-c, -n))

        value = 0                               # sum of top x elements
        high = []                               # heap for top x most frequent/largest elements
        high_nums = set()                       # keeps numbers currently in top x heap

        # pick top x elements from low into high
        while len(high_nums) < x and low:
            c, n = heapq.heappop(low)           # get element with highest count/value
            heapq.heappush(high, (-c, -n))      # push into top heap (convert signs back)
            high_nums.add(-n)                   # mark number as part of top x
            value += c * n                      # add its contribution (note: both c, n are negative)

        res.append(value)                       # store x-sum for the first window

        # helper: decide where to place updated element based on its set
        def process_num(num):
            if num in high_nums:                # if number is in top x
                heapq.heappush(high, (counts[num], num))  # push to top heap
            else:
                heapq.heappush(low, (-counts[num], -num)) # else to low heap

        # remove invalid or outdated entries from low heap
        def clean_low():
            while low and (counts[-low[0][1]] != -low[0][0] or -low[0][1] in high_nums):
                heapq.heappop(low)              # pop wrong entries

        # remove invalid or outdated entries from high heap
        def clean_high():
            while high and (counts[high[0][1]] != high[0][0] or high[0][1] not in high_nums):
                heapq.heappop(high)

        # slide the window across the array
        for i in range(k, len(nums)):
            leaving = nums[i - k]               # element going out of window
            entering = nums[i]                  # element coming into window

            if leaving == entering:             # if both same, skip updates
                res.append(value)
                continue

            counts[leaving] -= 1                # decrease freq of outgoing element
            counts[entering] += 1               # increase freq of incoming element

            if leaving in high_nums:            # if leaving number was in top x
                value -= leaving                # subtract its contribution

            if entering in high_nums:           # if entering number already in top x
                value += entering               # add its contribution

            process_num(leaving)                # push updated leaving number into proper heap
            process_num(entering)               # push updated entering number into proper heap

            clean_low()                         # clean outdated entries in low
            clean_high()                        # clean outdated entries in high

            # check if a better element in low should replace weaker one in high
            if low and high:
                if -low[0][0] > high[0][0] or (-low[0][0] >= high[0][0] and -low[0][1] > high[0][1]):
                    new_count, new_high = heapq.heappop(low)   # pop best from low
                    old_count, old_high = heapq.heappop(high)  # pop worst from high
                    high_nums.remove(old_high)                 # update set
                    high_nums.add(-new_high)

                    # update total sum by removing old and adding new element
                    value -= (old_high * counts[old_high])
                    value += (-new_high * counts[-new_high])

                    # push them back into correct heaps
                    heapq.heappush(high, (-new_count, -new_high))
                    heapq.heappush(low, (-old_count, -old_high))

            clean_low()                         # recheck low for outdated entries

            # if we have less than x elements in high, fill it from low
            if low and len(high_nums) < x:
                new_count, new_high = heapq.heappop(low)
                value += (-new_high * counts[-new_high])       # add its contribution
                heapq.heappush(high, (-new_count, -new_high))  # push into high heap
                high_nums.add(-new_high)                       # mark in top x set

            res.append(value)                    # store x-sum for this window

        return res                              # return list of all x-sums
