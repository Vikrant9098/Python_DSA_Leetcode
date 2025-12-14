class Solution:                              # Define the Solution class
    def numberOfWays(self, corridor):        # Function to count valid ways
        MOD = 10**9 + 7                      # Mod value to avoid overflow

        zero = 0                             # Ways with 0 seats in current section
        one = 0                              # Ways with 1 seat in current section
        two = 1                              # Ways with 2 seats (valid section)

        for thing in corridor:               # Loop through each character
            if thing == 'S':                 # If the character is a seat
                zero = one                  # Move 1-seat ways to 0-seat
                one, two = two, one          # Shift states for seat count
            else:                            # If the character is a plant
                two = (two + zero) % MOD     # Add ways by placing divider

        return zero                          # Return total valid ways
