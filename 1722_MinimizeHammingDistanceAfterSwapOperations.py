class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """

        # -------- Union Find (Disjoint Set) Definition --------
        class UnionFind(object):
            def __init__(self, n):
                # Initially, every node is its own parent
                self.fa = list(range(n))
                # Rank is used to keep tree shallow
                self.rank = [0] * n

            def find(self, x):
                # Path compression: make parent directly root
                if self.fa[x] != x:
                    self.fa[x] = self.find(self.fa[x])
                return self.fa[x]

            def union(self, x, y):
                # Find root of both nodes
                x = self.find(x)
                y = self.find(y)

                # If already in same set, do nothing
                if x == y:
                    return

                # Union by rank (attach smaller tree under larger)
                if self.rank[x] < self.rank[y]:
                    x, y = y, x

                self.fa[y] = x  # attach y under x

                # If ranks are equal, increase rank of new root
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1

        from collections import defaultdict

        n = len(source)

        # Initialize UnionFind
        uf = UnionFind(n)

        # Step 1: Merge indices that can be swapped
        for a, b in allowedSwaps:
            uf.union(a, b)

        # Step 2: Group values of 'source' by connected components
        # sets[root][value] = frequency of that value in this component
        sets = defaultdict(lambda: defaultdict(int))

        for i in range(n):
            root = uf.find(i)              # find component leader
            sets[root][source[i]] += 1     # count occurrence of source[i]

        # Step 3: Try matching with target
        ans = 0

        for i in range(n):
            root = uf.find(i)  # component leader

            # If target value exists in this component
            if sets[root][target[i]] > 0:
                sets[root][target[i]] -= 1  # use one occurrence
            else:
                ans += 1  # mismatch → contributes to Hamming distance

        return ans