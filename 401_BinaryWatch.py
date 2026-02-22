class Solution(object):   # Define the Solution class
    def readBinaryWatch(self, turnedOn):   # Function that returns all possible times with 'turnedOn' LEDs
        
        if turnedOn < 0 or turnedOn > 10:  # If LEDs are invalid (less than 0 or more than total 10 LEDs)
            return []                      # Return empty list
        
        result = []   # List to store valid time strings
        
        for h in range(12):   # Loop through all possible hours (0 to 11)
            for m in range(60):   # Loop through all possible minutes (0 to 59)
                
                # Count number of 1s in binary of hour and minute
                # If total 1s equals turnedOn LEDs
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    
                    # Format time as "hour:minute" (minute always 2 digits)
                    result.append("{}:{:02d}".format(h, m))
        
        return result   # Return all valid times
