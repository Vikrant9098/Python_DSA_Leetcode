class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """

        found = True                # flag to check if value is found

        while found:                # repeat until value is not found
            found = False           # assume value is not found

            for num in nums:        # go through each number in the list
                if num == original: # if number equals original
                    original *= 2   # multiply original by 2
                    found = True    # mark found to repeat loop
                    break           # stop checking further

        return original             # return final value
