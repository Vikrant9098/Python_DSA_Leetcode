class Solution(object):
    def numberOfSubstrings(self, s):
        result = 0  # total dominant substrings
        last_zero_indices = [-1]  # store positions of '0' (start with -1 for easy calc)
        n = len(s)  # length of string

        for i in range(n):  # loop through each character
            ch = s[i]  # current character
            count_ones = count_zeros = 0  # counts for current substring
            
            if ch == '1':
                count_ones += 1  # first char is 1
            else:
                count_zeros += 1  # first char is 0
            
            p = i  # start from current index
            
            for v in reversed(last_zero_indices):  # go backwards over zero positions
                count_ones += p - v - 1  # ones between p and previous zero
                result += max(0, min(p - v, count_ones - count_zeros**2 + 1))  
                # add number of dominant substrings ending at i

                p = v  # move pointer to previous zero position
                count_zeros += 1  # add this zero to count
                
                if count_zeros**2 > i:  # if zeros already too many, stop
                    break
            
            if ch == '0':
                last_zero_indices.append(i)  # store index of 0
        
        return result  # final result
