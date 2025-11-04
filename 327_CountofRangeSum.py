class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # build prefix sum array with 0 at start
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)  # add cumulative sum

        # helper function for counting valid range sums
        def merge_sort(left, right):
            # base case: single element has no range
            if right - left <= 1:
                return 0

            mid = (left + right) // 2  # find middle index

            # count in both halves
            count = merge_sort(left, mid) + merge_sort(mid, right)

            j = k = mid  # pointers for valid range
            temp = []    # temp array for merge
            r = mid      # pointer for merging

            # loop through left half
            for i in range(left, mid):
                # move k to first valid prefix (>= lower)
                while k < right and prefix[k] - prefix[i] < lower:
                    k += 1
                # move j to first invalid prefix (> upper)
                while j < right and prefix[j] - prefix[i] <= upper:
                    j += 1
                # count valid ones
                count += j - k

                # merge step: add smaller right elements
                while r < right and prefix[r] < prefix[i]:
                    temp.append(prefix[r])
                    r += 1
                # add current left element
                temp.append(prefix[i])

            # copy remaining right elements
            temp.extend(prefix[r:right])
            # put merged result back
            prefix[left:right] = temp

            # return total count
            return count

        # return total valid range count
        return merge_sort(0, len(prefix))
