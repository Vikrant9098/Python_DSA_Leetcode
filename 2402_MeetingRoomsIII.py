class Solution(object):

    def mostBooked(self, n, meetings):

        meetings.sort()                  # Sort meetings by start time

        count = [0] * n                  # count[i] = meetings booked in room i
        timer = [0] * n                  # timer[i] = when room i becomes free

        itr = 0                          # index to loop through meetings

        # Process each meeting
        while itr < len(meetings):

            start, end = meetings[itr]   # get start and end time
            dur = end - start            # duration of meeting

            room = -1                    # selected free room
            earliest = float('inf')      # earliest free time
            earliestRoom = -1            # room with earliest free time

            # Check all rooms
            for i in range(n):

                # Track room that frees earliest
                if timer[i] < earliest:
                    earliest = timer[i]
                    earliestRoom = i

                # If room is free before meeting starts
                if timer[i] <= start:
                    room = i
                    break                # stop checking more rooms

            # If a free room was found
            if room != -1:
                timer[room] = end        # update free time
                count[room] += 1         # increase meeting count
            else:
                timer[earliestRoom] += dur  # delay meeting to earliest room
                count[earliestRoom] += 1    # increase meeting count

            itr += 1                     # move to next meeting

        maxv = 0                         # maximum meetings
        idx = 0                          # room index with max meetings

        # Find room used the most
        for i in range(n):
            if count[i] > maxv:
                maxv = count[i]
                idx = i

        return idx                       # return most booked room
