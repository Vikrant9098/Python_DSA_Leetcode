class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """

        # Convert the hour hand position into hour units.
        # Example: at 3:30, the hour hand is at 3.5 hours.
        x = hour + minutes / 60.0

        # Difference between hour hand and minute hand in hour units.
        # Minute hand position in hour units = minutes / 5 = x - hour + ...
        # Simplified formula: (11 * x) % 12
        diff = (11 * x) % 12

        # Take the smaller angle between the two hands.
        # Convert hour-unit difference to degrees (1 hour unit = 30 degrees).
        return min(diff, 12 - diff) * 30