class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)  # get length of the string
        
        # try all possible first and second number splits
        for i in range(1, n // 2 + 1):
            # skip if first number starts with 0 and has more digits
            if num[0] == '0' and i > 1:
                break
            
            first = int(num[:i])  # first number
            
            # try all possible second numbers
            for j in range(i + 1, n):
                # skip if second number starts with 0 and has more digits
                if num[i] == '0' and j - i > 1:
                    break
                
                second = int(num[i:j])  # second number
                
                # check if rest of string is valid additive sequence
                if self.isValid(first, second, num[j:]):
                    return True
        
        return False  # no valid sequence found

    def isValid(self, first, second, remaining):
        # keep checking next sums
        while remaining:
            sum_ = first + second  # next number
            sum_str = str(sum_)  # convert sum to string
            
            # if remaining doesn’t start with sum string, invalid
            if not remaining.startswith(sum_str):
                return False
            
            # remove used part from remaining string
            remaining = remaining[len(sum_str):]
            
            # move to next numbers
            first, second = second, sum_
        
        return True  # valid additive sequence
