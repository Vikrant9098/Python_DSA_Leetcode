class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        # Start at altitude 0
        current_altitude = 0
        highest_altitude = 0
        
        # Process each gain to calculate altitude at each point
        for altitude_gain in gain:
            # Add gain to current altitude
            current_altitude += altitude_gain
            
            # Update highest altitude if current is higher
            highest_altitude = max(highest_altitude, current_altitude)
        
        # Return the highest altitude encountered
        return highest_altitude