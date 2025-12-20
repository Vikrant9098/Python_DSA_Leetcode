# Import defaultdict and deque
from collections import defaultdict, deque

# Solution class
class Solution:

    # Function to find all people who know the secret
    def findAllPeople(self, n, meet, fp):

        # Dictionary to group meetings by time
        timeMeetings = defaultdict(list)

        # Loop through all meetings
        for x, y, t in meet:

            # Store meeting pair at time t
            timeMeetings[t].append((x, y))

        # ks means "knows secret"
        ks = [False] * n

        # Person 0 knows the secret initially
        ks[0] = True

        # firstPerson also knows the secret
        ks[fp] = True

        # Process meetings in increasing time order
        for t in sorted(timeMeetings.keys()):

            # Get meetings at time t
            meetings = timeMeetings[t]

            # Adjacency list for meetings at time t
            meetList = defaultdict(list)

            # Build graph connections for time t
            for x, y in meetings:

                # x can talk to y
                meetList[x].append(y)

                # y can talk to x
                meetList[y].append(x)

            # Set of people who start spreading secret
            start = set()

            # Find people who already know the secret
            for x, y in meetings:

                # If x knows the secret
                if ks[x]:

                    # Add x as BFS start
                    start.add(x)

                # If y knows the secret
                if ks[y]:

                    # Add y as BFS start
                    start.add(y)

            # Queue for BFS
            q = deque(start)

            # BFS to spread the secret
            while q:

                # Take one person from queue
                person = q.popleft()

                # Check all people met by this person
                for nextPerson in meetList[person]:

                    # If next person does not know secret
                    if not ks[nextPerson]:

                        # Mark secret as known
                        ks[nextPerson] = True

                        # Add person to queue
                        q.append(nextPerson)

        # Return all people who know the secret
        return [i for i in range(n) if ks[i]]
