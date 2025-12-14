class Solution(object):
    def countMentions(self, numberOfUsers, events):
        """
        :type numberOfUsers: int
        :type events: List[List[str]]
        :rtype: List[int]
        """

        sorted_dict=[]
        # List to store events with sorting info

        for index, event in enumerate(events):
            timestamp = int(event[1])
            # Convert event time to int

            evetype = 0 if event[0] == "OFFLINE" else 1
            # OFFLINE = 0, MESSAGE = 1 (so OFFLINE comes first if same time)

            sorted_dict.append((timestamp, evetype, index))
            # Store: (time, type, original index)

        sorted_dict.sort(key=lambda x: (x[0], x[1], x[2]))
        # Sort by time, then by type, then by original index

        print(sorted_dict)
        # Debug print (shows sorted order)

        mentions = [0] * numberOfUsers
        # Store final mention count for each user

        offline = [0] * numberOfUsers
        # Store when each user becomes online again

        for vals in sorted_dict:
            index = vals[2]
            # Get original event index

            origin = events[index]
            # Access original event data

            eveType = origin[0]
            # Event type: MESSAGE or OFFLINE

            if eveType == "OFFLINE":
                id = int(origin[2])
                # User ID going offline

                timestamp = int(origin[1])
                # Time of offline event

                offline[id] = timestamp + 60
                # User will come online after 60 seconds

            else:
                timestamp = int(origin[1])
                # Message time

                menString = origin[2].split()
                # Split mentions inside message

                for men in menString:
                    if men[0] == 'i':
                        # Direct mention like "id5"
                        id = int(men[2:])
                        mentions[id] += 1

                    if men == "ALL":
                        # ALL → mention everyone
                        for k in range(numberOfUsers):
                            mentions[k] += 1

                    if men == "HERE":
                        # HERE → mention only online users
                        for k in range(numberOfUsers):
                            if timestamp >= offline[k]:
                                # User is online (not inside cooldown)
                                mentions[k] += 1

        return mentions
        # Return final result
