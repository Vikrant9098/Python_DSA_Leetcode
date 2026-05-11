class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # Store the final separated digits
        res = []

        # Traverse each number in the input list
        for x in nums:
            tmp = []

            # Extract digits from the number
            while x > 0:
                tmp.append(x % 10)   # Get last digit
                x //= 10             # Remove last digit

            # Reverse to maintain original digit order
            res.extend(tmp[::-1])

        return res