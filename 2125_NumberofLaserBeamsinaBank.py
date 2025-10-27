class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        # Count of beams
        total_beams = 0
        
        # Variable to store number of devices in the previous non-empty row
        prev_devices = 0
        
        # Loop through each row in the bank
        for row in bank:
            # Count how many '1's (devices) are in the current row
            curr_devices = row.count('1')
            
            # If current row has no device, skip it
            if curr_devices == 0:
                continue
            
            # Multiply devices in current and previous rows
            # because each device in previous row connects with all devices in current row
            total_beams += prev_devices * curr_devices
            
            # Update previous device count for next calculation
            prev_devices = curr_devices
        
        # Return the total number of beams
        return total_beams
