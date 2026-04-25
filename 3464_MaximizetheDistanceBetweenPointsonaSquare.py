from bisect import bisect_left

class Solution(object):
    def maxDistance(self, side, points, k):
        """
        :type side: int
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        # Step 1: Convert 2D boundary points into a 1D representation
        # We map the square boundary to a linear "perimeter" (0 to 4*side)
        arr = []
        
        for x, y in points:
            if x == 0:
                # Left edge → distance from bottom-left corner going upwards
                arr.append(y)
            elif y == side:
                # Top edge → continue from left edge
                arr.append(side + x)
            elif x == side:
                # Right edge → continue from top edge
                arr.append(side * 3 - y)
            else:
                # Bottom edge → continue from right edge
                arr.append(side * 4 - x)
        
        # Step 2: Sort the linear positions
        arr.sort()
        
        # Step 3: Helper function to check if we can place k points
        # such that minimum distance between consecutive points is at least 'limit'
        def check(limit):
            perimeter = side * 4  # total perimeter
            
            # Try each point as a starting point
            for start in arr:
                end = start + perimeter - limit  # max allowed range
                
                cur = start  # current selected point
                
                # Try to pick remaining (k-1) points
                for _ in range(k - 1):
                    # Find next point with at least 'limit' distance
                    idx = bisect_left(arr, cur + limit)
                    
                    # If no valid point found OR exceeds allowed range → fail
                    if idx == len(arr) or arr[idx] > end:
                        cur = -1
                        break
                    
                    # Move to next valid point
                    cur = arr[idx]
                
                # If we successfully picked k points → return True
                if cur >= 0:
                    return True
            
            # If no valid configuration found
            return False
        
        # Step 4: Binary search on the answer (minimum distance)
        lo, hi = 1, side  # distance range
        ans = 0
        
        while lo <= hi:
            mid = (lo + hi) // 2  # candidate distance
            
            if check(mid):
                # If possible, try for a larger distance
                ans = mid
                lo = mid + 1
            else:
                # Otherwise, reduce the distance
                hi = mid - 1
        
        # Final answer → maximum minimum distance
        return ans