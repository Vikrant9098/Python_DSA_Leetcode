class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1  # start and end pointers

        # swap characters until pointers meet
        while left < right:
            s[left], s[right] = s[right], s[left]  # swap elements
            left += 1   # move left forward
            right -= 1  # move right backward
