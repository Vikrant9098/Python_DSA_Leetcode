class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """

        # Create a list to store all elements from the grid
        nums_array = []
        result = 0

        # Flatten the 2D grid into a 1D list
        for row in grid:
            for num in row:
                nums_array.append(num)

        # Sort the array to easily find the median
        nums_array.sort()

        length = len(nums_array)

        # Choose the median as the target value (minimizes total operations)
        final_common_number = nums_array[length // 2]

        # Iterate through each number in the flattened list
        for number in nums_array:

            # If it's impossible to convert (different remainder mod x), return -1
            if number % x != final_common_number % x:
                return -1

            # Count operations needed to convert current number to median
            result += abs(final_common_number - number) // x

        return result