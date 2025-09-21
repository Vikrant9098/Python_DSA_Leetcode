from sortedcontainers import SortedList   # Import SortedList (keeps elements sorted)

class MovieRentingSystem:
    def __init__(self, n, entries):
        # Dictionary: movie -> SortedList of (price, shop)
        self.shops = defaultdict(SortedList)
        # Dictionary: (shop, movie) -> price
        self.shop_movie = {}
        # SortedList of rented movies (price, shop, movie)
        self.rented = SortedList()

        # Fill data structures with initial entries
        for s, m, p in entries:
            self.shops[m].add((p, s))      # Add (price, shop) to available list of movie m
            self.shop_movie[s, m] = p      # Save price for quick lookup

    def search(self, movie):
        # Return up to 5 shops with this movie, cheapest first
        return [y for _, y in self.shops[movie][:5]]

    def rent(self, shop, movie):
        price = self.shop_movie[shop, movie]       # Get price
        self.shops[movie].remove((price, shop))    # Remove from available list
        self.rented.add((price, shop, movie))      # Add to rented list

    def drop(self, shop, movie):
        price = self.shop_movie[shop, movie]       # Get price
        self.shops[movie].add((price, shop))       # Add back to available list
        self.rented.remove((price, shop, movie))   # Remove from rented list

    def report(self):
        # Return up to 5 rented movies as [shop, movie]
        return [[y, z] for _, y, z in self.rented[:5]]
