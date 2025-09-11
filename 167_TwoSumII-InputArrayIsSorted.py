class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1  # Two pointers: start and end

        while left < right:
            total = numbers[left] + numbers[right]  # Current sum of two numbers

            if total == target:
                # Found the pair -> return 1-based indices
                return [left + 1, right + 1]
            elif total < target:
                left += 1  # Need bigger sum -> move left pointer right
            else:
                right -= 1  # Need smaller sum -> move right pointer left

        # Not expected (problem guarantees one solution)
        return [-1, -1]
