class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """

        def maxSubsequence(nums, k):  # get biggest subsequence of length k
            stack = []  # to store chosen digits
            to_remove = len(nums) - k  # how many digits can be removed
            for num in nums:  # go through each number
                while stack and stack[-1] < num and to_remove > 0:  # remove smaller digits
                    stack.pop()  # remove top
                    to_remove -= 1  # one removed
                stack.append(num)  # add current digit
            return stack[:k]  # keep only first k digits

        def merge(nums1, nums2):  # merge two lists to make max number
            result = []  # final merged list
            while nums1 or nums2:  # until both empty
                if nums1 > nums2:  # pick bigger sequence
                    result.append(nums1.pop(0))  # take from nums1
                else:
                    result.append(nums2.pop(0))  # take from nums2
            return result  # return merged result

        best = []  # store best number
        m, n = len(nums1), len(nums2)  # lengths of both arrays

        # try all ways to split k between nums1 and nums2
        for i in range(max(0, k - n), min(k, m) + 1):
            part1 = maxSubsequence(nums1, i)      # take i digits from nums1
            part2 = maxSubsequence(nums2, k - i)  # take rest from nums2
            candidate = merge(part1[:], part2[:]) # merge both parts
            if candidate > best:  # check if candidate is larger
                best = candidate  # update best

        return best  # return final best number
