class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        # Sort both arrays to use greedy approach
        # We want to match smallest available player with smallest suitable trainer
        players.sort()
        trainers.sort()
        
        # Initialize pointers for both arrays
        player_idx = 0  # Points to current player we're trying to match
        trainer_idx = 0  # Points to current trainer we're checking
        
        # Counter for successful matchings
        matchings = 0
        
        # Continue until we've processed all players or all trainers
        while player_idx < len(players) and trainer_idx < len(trainers):
            # Check if current trainer can train current player
            if players[player_idx] <= trainers[trainer_idx]:
                # Match found! Current player can be trained by current trainer
                matchings += 1
                
                # Move to next player since current one is matched
                player_idx += 1
                
                # Move to next trainer since current one is now assigned
                trainer_idx += 1
            else:
                # Current trainer cannot train current player (trainer capacity too low)
                # Move to next trainer with higher capacity
                trainer_idx += 1
        
        # Return total number of successful matchings
        return matchings