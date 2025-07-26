class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        # Sort the products lexicographically
        products.sort()
        
        result = []               # Final list to store suggestions after each character typed
        prefix = ''               # Initialize prefix as empty string

        # Iterate through each character of the search word
        for ch in searchWord:
            prefix += ch          # Build prefix incrementally
            suggestions = []      # List to store up to 3 matching suggestions
            
            # Check each product in sorted list
            for product in products:
                # If product starts with current prefix
                if product.startswith(prefix):
                    suggestions.append(product)  # Add to suggestions
                    if len(suggestions) == 3:    # Stop after collecting 3 products
                        break
            
            result.append(suggestions)  # Add current suggestions to result
        
        return result
