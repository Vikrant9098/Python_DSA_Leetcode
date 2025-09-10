class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # If there are less than 3 bars, no water can be trapped
        if len(height) < 3:
            return 0

        # Initialize two pointers, one starting from left, one from right
        left, right = 0, len(height) - 1

        # Track the maximum height seen so far from both sides
        left_max, right_max = height[left], height[right]

        # Result variable to store total trapped water
        water = 0

        # Process until left and right pointers meet
        while left < right:
            # If left side is smaller, move from left
            if left_max < right_max:
                left += 1
                # Update left max if new bar is higher
                left_max = max(left_max, height[left])
                # Water trapped at this bar is left_max - current height
                water += left_max - height[left]
            else:
                # Otherwise move from right side
                right -= 1
                # Update right max if new bar is higher
                right_max = max(right_max, height[right])
                # Water trapped at this bar is right_max - current height
                water += right_max - height[right]

        return water
