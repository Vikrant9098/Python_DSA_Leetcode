class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        ans = []  # This will store the final valid queries
        
        # Loop through each query word
        for query in queries:
            
            # Compare current query with every word in dictionary
            for s in dictionary:
                dis = 0  # Count of different characters
                
                # Compare character by character
                for i in range(len(query)):
                    if query[i] != s[i]:  # If characters don't match
                        dis += 1          # Increase difference count
                
                # If difference is at most 2 → valid query
                if dis <= 2:
                    ans.append(query)  # Add query to answer
                    break              # No need to check other dictionary words
        
        return ans  # Return all valid queries
