class Solution(object):
    def canMeasureWater(self, x, y, target):
        """
        :type x: int
        :type y: int
        :type target: int
        :rtype: bool
        """
        # if total capacity is less than target, impossible
        if x + y < target:
            return False
        
        # if target is 0, it's trivially possible
        if target == 0:
            return True
        
        # check if target is multiple of gcd(x, y)
        return target % self.gcd(x, y) == 0

    # helper function to find gcd (greatest common divisor)
    def gcd(self, a, b):
        while b != 0:       # continue until remainder becomes 0
            a, b = b, a % b # update a and b
        return a            # return gcd
