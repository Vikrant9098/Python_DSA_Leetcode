class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # Step 1: Sort the input array to use the two-pointer approach
        nums.sort()

        # Step 2: Initialize the result with the sum of the first three numbers
        # This acts as our starting "closest" sum
        closest = nums[0] + nums[1] + nums[2]

        # Step 3: Traverse each number in the array
        for i in range(len(nums) - 2):

            # Step 4: Initialize two pointers, one just after `i`, and one at the end
            left = i + 1
            right = len(nums) - 1

            # Step 5: While left pointer is to the left of right pointer
            while left < right:
                # Calculate the current triplet sum
                current_sum = nums[i] + nums[left] + nums[right]

                # Step 6: Check if this current sum is closer to the target than previous closest
                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum  # Update the closest sum

                # Step 7: If the current sum is exactly equal to target, return it immediately
                if current_sum == target:
                    return target
                # Step 8: If current sum is less than target, move left to get a larger value
                elif current_sum < target:
                    left += 1
                # Step 9: If current sum is greater than target, move right to get a smaller value
                else:
                    right -= 1

        # Step 10: After checking all possibilities, return the closest sum found
        return closest
