class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sum_val = 0  # store total sum of array

        rem1 = []  # list for numbers giving remainder 1
        rem2 = []  # list for numbers giving remainder 2

        for num in nums:            # loop through each number
            sum_val += num          # add number to total sum

            if num % 3 == 1:        # if remainder is 1
                rem1.append(num)    # add to rem1 list
            elif num % 3 == 2:      # if remainder is 2
                rem2.append(num)    # add to rem2 list

        if sum_val % 3 == 0:        # if divisible by 3
            return sum_val          # return directly

        rem1.sort()                 # sort rest 1 list (smallest first)
        rem2.sort()                 # sort rest 2 list

        remainder = sum_val % 3     # get remainder of full sum

        if remainder == 1:          # if remainder is 1
            option1 = sum_val - rem1[0] if len(rem1) >= 1 else 0  # remove smallest rem1
            option2 = sum_val - rem2[0] - rem2[1] if len(rem2) >= 2 else 0  # or two from rem2
            return max(option1, option2)  # return maximum
        else:                       # remainder must be 2
            option1 = sum_val - rem2[0] if len(rem2) >= 1 else 0  # remove smallest rem2
            option2 = sum_val - rem1[0] - rem1[1] if len(rem1) >= 2 else 0  # or two from rem1
            return max(option1, option2)  # return max result
