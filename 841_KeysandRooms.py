class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        # Create a set to keep track of visited rooms
        visited = set()

        # Define a recursive DFS function to explore rooms
        def dfs(room):
            # If this room is already visited, return
            if room in visited:
                return

            # Mark the room as visited
            visited.add(room)

            # Explore all keys (i.e., next rooms) in the current room
            for key in rooms[room]:
                dfs(key)

        # Start DFS from room 0
        dfs(0)

        # Check if all rooms have been visited
        return len(visited) == len(rooms)
