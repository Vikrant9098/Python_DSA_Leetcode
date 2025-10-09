class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []  # list to build the resulting binary string
        i, j = len(a) - 1, len(b) - 1  # pointers starting from the end of a and b
        carry = 0  # carry for binary addition

        # loop until both strings are processed and no carry left
        while i >= 0 or j >= 0 or carry:
            sum_val = carry  # start sum with the current carry

            if i >= 0:  # if a has remaining digits
                sum_val += int(a[i])  # add current digit of a to sum
                i -= 1  # move pointer left in a
            if j >= 0:  # if b has remaining digits
                sum_val += int(b[j])  # add current digit of b to sum
                j -= 1  # move pointer left in b

            result.append(str(sum_val % 2))  # append the current binary digit (0 or 1)
            carry = sum_val // 2  # update carry for next iteration

        return ''.join(result[::-1])  # reverse the result list and join to form final string
