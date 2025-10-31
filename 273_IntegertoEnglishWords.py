class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        # If number is 0, directly return "Zero"
        if num == 0:
            return "Zero"
        
        # Words for numbers below 20
        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
                    "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", 
                    "Eighteen", "Nineteen"]
        
        # Words for tens (20, 30, 40, ...)
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        # Words for thousand groups
        thousands = ["", "Thousand", "Million", "Billion"]

        # Helper function to convert numbers less than 1000 into words
        def helper(n):
            # If number is 0, return empty string
            if n == 0:
                return ""
            # If number is less than 20, return its word
            elif n < 20:
                return below_20[n] + " "
            # If number is less than 100, get tens and ones
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            # If number is 100 or more, get hundreds part and remaining part
            else:
                return below_20[n // 100] + " Hundred " + helper(n % 100)
        
        res = ""  # To store the final result
        i = 0     # Index for thousands group
        
        # Process number in groups of 3 digits (thousands, millions, billions)
        while num > 0:
            # If current group is not zero
            if num % 1000 != 0:
                # Convert this group and add its thousand word
                res = helper(num % 1000) + thousands[i] + " " + res
            # Move to next group (next 3 digits)
            num //= 1000
            i += 1
        
        # Remove extra spaces and return final result
        return res.strip()
