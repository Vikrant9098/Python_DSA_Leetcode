class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)       # length of the array
        ans = 0             # count of valid selections

        for i in range(n):
            if nums[i] == 0:  # can only start from zero
                # try moving left
                if self.canZeroAll(nums, i, -1):
                    ans += 1
                # try moving right
                if self.canZeroAll(nums, i, 1):
                    ans += 1

        return ans           # return total valid selections

    def canZeroAll(self, nums, start, direction):
        arr = nums[:]        # make a copy of the list
        n = len(arr)
        curr = start         # current index

        # keep moving while inside bounds
        while 0 <= curr < n:
            if arr[curr] == 0:
                curr += direction        # move in same direction
            else:
                arr[curr] -= 1           # decrease element by 1
                direction *= -1          # reverse direction
                curr += direction        # move one step in new direction

        # check if all elements became 0
        for val in arr:
            if val != 0:
                return False
        return True
