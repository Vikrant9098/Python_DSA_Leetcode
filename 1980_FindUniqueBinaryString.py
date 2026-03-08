class Solution(object):
    def findDifferentBinaryString(self, nums):
        
        ans = ''   # Initialize an empty string to store the resulting binary string
        
        # enumerate(nums) gives both index (i) and the string (num)
        for i, num in enumerate(nums):
            
            # Take the ith character from the ith binary string
            # If the bit is '0', append '1'
            # If the bit is '1', append '0'
            # This flips the diagonal bit to ensure the result differs from nums[i]
            ans += '1' if (num[i] == '0') else '0'   # ternary if-else operator
        
            # Alternate approach:
            # Convert the bit to integer, subtract from 1 to flip (0->1, 1->0),
            # then convert back to string before appending
            # ans += str(1 - int(num[i]))

        # The constructed string differs from every nums[i] at index i
        # so it is guaranteed not to exist in the input list
        return ans