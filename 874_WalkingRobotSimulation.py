class Solution:
    def robotSim(self, commands, obstacles):
        
        # Convert obstacles list into a set for O(1) lookup
        st = set()
        for x, y in obstacles:
            st.add((x, y))

        # दिशा (direction vectors):
        # 0 -> North (0,1)
        # 1 -> East  (1,0)
        # 2 -> South (0,-1)
        # 3 -> West  (-1,0)
        dir = [(0,1), (1,0), (0,-1), (-1,0)]

        # Robot starts at origin (0,0)
        x = y = 0
        
        # Initial direction = North (index 0)
        d = 0
        
        # Store maximum distance squared from origin
        maxDist = 0

        # Process each command
        for cmd in commands:
            
            # Turn right (clockwise)
            if cmd == -1:
                d = (d + 1) % 4
            
            # Turn left (anti-clockwise)
            elif cmd == -2:
                d = (d + 3) % 4   # same as (d - 1 + 4) % 4
            
            # Move forward cmd steps
            else:
                for _ in range(cmd):
                    
                    # Calculate next position
                    nx = x + dir[d][0]
                    ny = y + dir[d][1]

                    # If next position is an obstacle → stop moving further
                    if (nx, ny) in st:
                        break

                    # Otherwise move to next position
                    x, y = nx, ny

                    # Update maximum distance squared
                    # (x^2 + y^2 is used instead of sqrt for efficiency)
                    maxDist = max(maxDist, x*x + y*y)

        # Return the maximum distance squared from origin
        return maxDist