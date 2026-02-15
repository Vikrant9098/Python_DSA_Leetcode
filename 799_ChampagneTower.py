class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        
        # Create a 2D list where each row has (row_index + 1) glasses
        tower = [[0] * (i + 1) for i in range(query_row + 1)]
        
        # Pour all champagne into the top glass
        tower[0][0] = poured

        # Iterate through each row until the required query_row
        for row in range(query_row):
            for glass in range(len(tower[row])):
                
                # Calculate excess champagne (only overflow above 1 cup)
                excess = (tower[row][glass] - 1) / 2.0
                
                # If there is overflow, distribute equally to next row
                if excess > 0:
                    tower[row + 1][glass] += excess
                    tower[row + 1][glass + 1] += excess

        # A glass can hold maximum 1 cup
        return min(1.0, tower[query_row][query_glass])
