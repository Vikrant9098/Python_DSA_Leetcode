class Solution(object):
    def replaceNonCoprimes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # custom gcd function (Euclidean algorithm)
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        stack = []  # stack to keep final numbers step by step

        for num in nums:  
            stack.append(num)  # add number to stack

            # keep merging while last two numbers are non-coprime
            while len(stack) > 1 and gcd(stack[-1], stack[-2]) > 1:
                a = stack.pop()   # take last number
                b = stack.pop()   # take second last number

                # find LCM of a and b
                lcm = (a * b) // gcd(a, b)

                stack.append(lcm)  # put LCM back to stack

        return stack  # return final modified array
