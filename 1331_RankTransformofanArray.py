class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        # Dictionary to store each unique number and its rank
        num_to_rank = {}

        # Create a sorted copy of the array
        sorted_arr = sorted(arr)

        # Rank starts from 1
        rank = 1

        # Traverse the sorted array
        for i in range(len(sorted_arr)):

            # Increase rank only when a new (greater) number is found
            if i > 0 and sorted_arr[i] > sorted_arr[i - 1]:
                rank += 1

            # Store the current number with its rank
            num_to_rank[sorted_arr[i]] = rank

        # Replace every element in the original array with its rank
        for i in range(len(arr)):
            arr[i] = num_to_rank[arr[i]]

        # Return the ranked array
        return arr