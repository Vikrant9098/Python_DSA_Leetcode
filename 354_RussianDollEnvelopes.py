class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # Sort envelopes by width ascending, and height descending if widths are same
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Extract only heights from the sorted envelopes
        heights = [h for _, h in envelopes]
        
        # Define helper function to find Longest Increasing Subsequence (LIS)
        def getLIS(nums):
            dp = []  # dp list will store the smallest ending value for LIS of each length
            for num in nums:  # Loop through each height
                left, right = 0, len(dp)  # Binary search boundaries
                while left < right:  # Binary search to find correct position
                    mid = (left + right) // 2  # Middle index
                    if dp[mid] < num:  # If mid value is smaller, go right
                        left = mid + 1
                    else:  # Else, go left
                        right = mid
                # If num is larger than all elements, append it
                if left == len(dp):
                    dp.append(num)
                else:  # Else replace the found position with current num
                    dp[left] = num
            return len(dp)  # Return LIS length
        
        # Call helper function on heights and return result
        return getLIS(heights)
