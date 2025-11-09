class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)  # total number of rows (and columns)
        
        left = matrix[0][0]  # smallest element in the matrix (top-left)
        right = matrix[n - 1][n - 1]  # largest element in the matrix (bottom-right)
        
        # perform binary search between smallest and largest number
        while left < right:
            mid = left + (right - left) // 2  # find middle value
            count = self.countLessEqual(matrix, mid, n)  # count numbers <= mid
            
            if count < k:
                # if count smaller than k, we need larger numbers
                left = mid + 1
            else:
                # else kth smallest is <= mid
                right = mid
        
        return left  # when left == right, it is the kth smallest number

    # helper function to count numbers <= mid
    def countLessEqual(self, matrix, mid, n):
        count = 0  # total count of numbers <= mid
        row = n - 1  # start from bottom-left corner
        col = 0  # start from first column
        
        # traverse the matrix efficiently
        while row >= 0 and col < n:
            if matrix[row][col] <= mid:
                # if current number <= mid,
                # then all numbers above it are also <= mid
                count += row + 1
                col += 1  # move right
            else:
                # if current number > mid, move up to smaller numbers
                row -= 1
        
        return count  # return total numbers <= mid
