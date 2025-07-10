class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Sort the array to enable two-pointer technique and skip duplicates
        nums.sort()
        
        # Store all unique quadruplets
        result = []
        
        # Get the length of array
        n = len(nums)
        
        # First loop: fix the first element
        for i in range(n - 3):  # Leave space for 3 more elements
            # Skip duplicate values for first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Second loop: fix the second element
            for j in range(i + 1, n - 2):  # Leave space for 2 more elements
                # Skip duplicate values for second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Use two pointers for remaining two elements
                left = j + 1
                right = n - 1
                
                # Two pointer approach for third and fourth elements
                while left < right:
                    # Calculate current sum of four elements
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    # If sum equals target, we found a valid quadruplet
                    if current_sum == target:
                        # Add the quadruplet to result
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates for third element
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        
                        # Skip duplicates for fourth element
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        # Move both pointers to find next potential quadruplet
                        left += 1
                        right -= 1
                    
                    # If sum is less than target, increase sum by moving left pointer
                    elif current_sum < target:
                        left += 1
                    
                    # If sum is greater than target, decrease sum by moving right pointer
                    else:
                        right -= 1
        
        # Return all unique quadruplets
        return result