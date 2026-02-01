class Solution(object):
    # Defines a class named Solution (required by platforms like LeetCode)

    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Method that takes a list of integers and returns the minimum cost

        a = 51
        # Variable to store the smallest value found (initialized to 51 as a safe maximum)

        b = 51
        # Variable to store the second smallest value found (also initialized to 51)

        for i in range(1, len(nums)):
            # Loop starts from index 1 because nums[0] is always included separately

            if nums[i] < a:
                # If current element is smaller than the smallest value found so far

                b = a
                # Move the previous smallest value into b (second smallest)

                a = nums[i]
                # Update a with the new smallest value

            elif nums[i] < b:
                # If current element is not smaller than a,
                # but smaller than the second smallest value b

                b = nums[i]
                # Update b with the new second smallest value

            if a == 1 and b == 1:
                # Since 1 is the smallest possible value,
                # once both smallest values are 1, no better result is possible

                break
                # Exit the loop early for optimization

        return nums[0] + a + b
        # Return the minimum cost:
        # first element + smallest value + second smallest value
