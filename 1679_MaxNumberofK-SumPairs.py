class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Method 1: Two pointers (after sorting)
        nums.sort()                 # Sort array first
        left = 0                    # Start pointer
        right = len(nums) - 1       # End pointer
        operations = 0              # Count operations
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == k:
                # Found pair that sums to k
                operations += 1
                left += 1           # Move both pointers
                right -= 1
            elif current_sum < k:
                # Sum too small, need larger number
                left += 1
            else:
                # Sum too large, need smaller number
                right -= 1
        
        return operations
    
    # Alternative method using hash map
    def maxOperations_hashmap(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter
        
        count = Counter(nums)       # Count frequency of each number
        operations = 0
        
        for num in count:
            complement = k - num    # Find complement
            
            if num == complement:
                # Special case: same number pairs (e.g., 3+3=6)
                operations += count[num] // 2
            elif complement in count and num < complement:
                # Avoid double counting by checking num < complement
                operations += min(count[num], count[complement])
        
        return operations

# Logic (Two Pointers):
# 1. Sort array to enable two-pointer technique
# 2. Use left and right pointers from both ends
# 3. If sum equals k: count operation, move both pointers
# 4. If sum < k: move left pointer (increase sum)
# 5. If sum > k: move right pointer (decrease sum)

# Test examples:
# nums = [1,2,3,4], k = 5
# After sorting: [1,2,3,4]
# left=0, right=3: 1+4=5 ✓ (operation 1)
# left=1, right=2: 2+3=5 ✓ (operation 2)
# Result: 2 operations