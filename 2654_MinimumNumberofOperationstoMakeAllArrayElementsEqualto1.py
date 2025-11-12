class Solution(object):
    def gcd(self, a, b):
        # find greatest common divisor (GCD) using Euclidean algorithm
        while b:  # loop till remainder becomes 0
            a, b = b, a % b  # update a and b
        return a  # return the gcd value

    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)  # get the length of the array
        
        ones_count = nums.count(1)  # count how many elements are 1
        if ones_count > 0:  # if there are already some 1s
            return n - ones_count  # only need to make others 1
        
        min_k = float('inf')  # store smallest subarray length with gcd = 1
        
        # check every subarray
        for i in range(n):
            current_g = nums[i]  # start gcd with current element
            for j in range(i + 1, n):  # move forward to form subarray
                current_g = self.gcd(current_g, nums[j])  # find gcd of subarray
                if current_g == 1:  # if gcd becomes 1
                    k = (j - i) + 1  # calculate subarray length
                    min_k = min(min_k, k)  # store minimum length
                    break  # break inner loop, gcd can't be smaller than 1
        
        if min_k == float('inf'):  # if no subarray has gcd = 1
            return -1  # impossible to make all elements 1
            
        ops_to_create_one = min_k - 1  # operations needed to create one 1
        ops_to_spread = n - 1  # operations to spread that 1 to all elements
        
        return ops_to_create_one + ops_to_spread  # total operations needed
