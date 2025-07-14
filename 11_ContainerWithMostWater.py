class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0                    # Start pointer at beginning
        right = len(height) - 1     # End pointer at end
        max_water = 0               # Track maximum area found
        
        while left < right:
            # Calculate current area
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            
            # Update maximum if current area is larger
            max_water = max(max_water, current_area)
            
            # Move pointer with smaller height (optimization)
            if height[left] < height[right]:
                left += 1           # Move left pointer right
            else:
                right -= 1          # Move right pointer left
        
        return max_water

# Alternative brute force solution (less efficient):
def maxArea_bruteforce(height):
    max_water = 0
    n = len(height)
    
    # Check all possible pairs
    for i in range(n):
        for j in range(i + 1, n):
            width = j - i
            current_height = min(height[i], height[j])
            area = width * current_height
            max_water = max(max_water, area)
    
    return max_water

# Logic:
# 1. Use two pointers (left and right) starting at ends
# 2. Calculate area = min(heights) * width
# 3. Move pointer with smaller height (can't improve by keeping it)
# 4. Continue until pointers meet, tracking maximum area

# Test examples:
# height = [1,8,6,2,5,4,8,3,7]
# Two pointers find heights 8 and 7 with width 7 → area = 7 * 7 = 49