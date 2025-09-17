from collections import defaultdict
import heapq

class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        # Map each food to its cuisine and current rating
        self.food_data = {}  # {food: (cuisine, rating)}
        
        # For each cuisine, maintain a max-heap of (-rating, food_name)
        # Using -rating because Python's heapq is a min-heap by default
        self.cuisine_heaps = defaultdict(list)
        
        # Initialize mappings and heaps with given data
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_data[food] = (cuisine, rating)  # store cuisine and rating
            heapq.heappush(self.cuisine_heaps[cuisine], (-rating, food))  
            # Push (-rating, food) into heap for that cuisine

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        # Get cuisine and old rating of this food
        cuisine, oldRating = self.food_data[food]
        
        # Update the rating in food_data
        self.food_data[food] = (cuisine, newRating)
        
        # Push the new rating into the heap of that cuisine
        heapq.heappush(self.cuisine_heaps[cuisine], (-newRating, food))
        # Note: we don’t remove the old rating, we just add the new one.
        # Old entries will be discarded lazily when popped.

    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        # Get the heap of this cuisine
        heap = self.cuisine_heaps[cuisine]
        
        # Check the top element of the heap
        # It may contain an outdated rating, so we keep popping until valid
        while True:
            rating, food = heap[0]  # peek at the top element (-rating, food)
            actual_cuisine, actual_rating = self.food_data[food]  # get current rating
            
            # If the rating matches, this is the correct highest-rated food
            if -rating == actual_rating:
                return food
            
            # Otherwise, pop outdated entry and continue
            heapq.heappop(heap)
