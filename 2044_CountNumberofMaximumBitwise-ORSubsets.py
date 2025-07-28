class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Find the maximum OR value that can be obtained from any subset
        max_or = 0
        for num in nums:
            max_or |= num  # Bitwise OR all elements to get the maximum possible OR
        
        self.count = 0  # Initialize the count of subsets that give max_or
        
        # Step 2: Backtrack through all subsets
        def backtrack(index, current_or):
            if index == len(nums):
                # If end of array reached, check if current OR equals max OR
                if current_or == max_or:
                    self.count += 1
                return
            
            # Include current number in the subset
            backtrack(index + 1, current_or | nums[index])
            
            # Exclude current number from the subset
            backtrack(index + 1, current_or)
        
        # Start backtracking from index 0 with OR value 0
        backtrack(0, 0)
        
        return self.count
