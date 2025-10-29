class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count1, count2 = 0, 0  # counts for two possible candidates
        candidate1, candidate2 = None, None  # store two potential majority elements

        # Step 1: Find potential candidates
        for num in nums:
            if candidate1 == num:
                count1 += 1  # increase count for candidate1
            elif candidate2 == num:
                count2 += 1  # increase count for candidate2
            elif count1 == 0:
                candidate1 = num  # assign new candidate1
                count1 = 1
            elif count2 == 0:
                candidate2 = num  # assign new candidate2
                count2 = 1
            else:
                count1 -= 1  # decrease both counts
                count2 -= 1

        # Step 2: Verify actual counts
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1  # count frequency of candidate1
            elif num == candidate2:
                count2 += 1  # count frequency of candidate2

        # Step 3: Add valid candidates to result
        result = []
        n = len(nums)
        if count1 > n // 3:
            result.append(candidate1)
        if count2 > n // 3:
            result.append(candidate2)

        return result  # return majority elements
