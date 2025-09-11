class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []  # Initialize a list to store all unique triplets that sum to 0
        nums.sort()  # Sort the array to make it easier to avoid duplicates and use two pointers

        # Iterate through the array, fixing one element at a time
        for i in range(len(nums) - 2):  # We stop at len(nums) - 2 because we need at least 3 numbers
            # Skip duplicate values for the first element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1  # Set two pointers: left (just after i) and right (end of list)

            # Use the two-pointer technique to find pairs that sum with nums[i] to 0
            while left < right:
                total = nums[i] + nums[left] + nums[right]  # Calculate the sum of the triplet

                if total == 0:
                    # Found a valid triplet, add it to result
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1  # Move left pointer to the right
                    right -= 1  # Move right pointer to the left

                    # Skip duplicate values for left pointer to avoid duplicate triplets
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicate values for right pointer to avoid duplicate triplets
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    # If the sum is too small, increase it by moving left pointer to the right
                    left += 1
                else:
                    # If the sum is too large, decrease it by moving right pointer to the left
                    right -= 1

        return res  # Return the list of all unique triplets
