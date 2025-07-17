class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # Use a stack to keep track of asteroids after collisions
        stack = []

        # Loop through each asteroid in the input
        for asteroid in asteroids:
            # Flag to check if the current asteroid should be pushed to stack
            alive = True

            # Continue checking collisions while the top of the stack is positive (moving right)
            # and current asteroid is negative (moving left)
            while stack and asteroid < 0 and stack[-1] > 0:
                top = stack[-1]

                if top < -asteroid:
                    # Top is smaller → it explodes
                    stack.pop()
                    # Keep checking next top
                elif top == -asteroid:
                    # Both are equal → both explode
                    stack.pop()
                    alive = False  # current asteroid also destroyed
                    break
                else:
                    # Current is smaller → it explodes
                    alive = False
                    break

            # If asteroid survived all collisions, push it to the stack
            if alive:
                stack.append(asteroid)

        return stack
