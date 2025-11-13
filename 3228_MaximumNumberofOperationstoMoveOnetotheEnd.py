class Solution(object):
    def maxOperations(self, s):
        result = 0        # stores total number of operations
        ones = 0          # counts number of '1's seen so far
        use = False       # flag to check if last seen was '0'
        
        for c in s:       # loop through each character in string
            if c == '0':  
                use = True    # mark that a '0' is found
            else:
                if use:       
                    result += ones   # add operations for previous '1's
                ones += 1            # count this '1'
                use = False          # reset flag since we saw '1'
        
        if use:              # if string ends with '0'
            result += ones   # add remaining operations
        
        return result        # return total operations
