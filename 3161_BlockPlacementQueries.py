class Solution(object):

    MAXX = 50000

    def __init__(self):

        # Segment tree to store maximum gap values
        self.seg = [0] * (4 * (self.MAXX + 1))

    def update(self, node, l, r, idx, val):

        # Leaf node reached
        if l == r:
            self.seg[node] = val
            return

        mid = (l + r) // 2

        # Go to left half
        if idx <= mid:
            self.update(2 * node, l, mid, idx, val)

        # Go to right half
        else:
            self.update(2 * node + 1, mid + 1, r, idx, val)

        # Store maximum value from children
        self.seg[node] = max(
            self.seg[2 * node],
            self.seg[2 * node + 1]
        )

    def query(self, node, l, r, ql, qr):

        # No overlap
        if ql > r or qr < l:
            return 0

        # Complete overlap
        if ql <= l and r <= qr:
            return self.seg[node]

        mid = (l + r) // 2

        # Return maximum from left and right halves
        return max(
            self.query(2 * node, l, mid, ql, qr),
            self.query(2 * node + 1, mid + 1, r, ql, qr)
        )

    def getResults(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[bool]
        """

        # Store all obstacle positions in sorted order
        obstacles = SortedSet([0])

        # Build final obstacle configuration
        for q in queries:

            # Type 1 query means add obstacle
            if q[0] == 1:
                obstacles.add(q[1])

        pos = list(obstacles)

        # Store gaps between consecutive obstacles
        for i in range(1, len(pos)):

            self.update(
                1,
                0,
                self.MAXX,
                pos[i],
                pos[i] - pos[i - 1]
            )

        ans = []

        # Process queries in reverse order
        for i in range(len(queries) - 1, -1, -1):

            # Type 2 query -> check if block can fit
            if queries[i][0] == 2:

                x = queries[i][1]
                sz = queries[i][2]

                # Find obstacle just before or equal to x
                idx = obstacles.bisect_right(x) - 1
                prev_obstacle = obstacles[idx]

                # Maximum gap before previous obstacle
                best = self.query(
                    1,
                    0,
                    self.MAXX,
                    0,
                    prev_obstacle
                )

                # Also consider current partial gap
                best = max(best, x - prev_obstacle)

                # Check if required size fits
                ans.append(best >= sz)

            else:

                # Reverse processing means removing obstacle
                x = queries[i][1]

                idx = obstacles.index(x)

                # Obstacle on left side
                left_pos = obstacles[idx - 1]

                # Remove gap ending at x
                self.update(1, 0, self.MAXX, x, 0)

                # If right obstacle exists
                if idx + 1 < len(obstacles):

                    right_pos = obstacles[idx + 1]

                    # Merge left and right gaps
                    self.update(
                        1,
                        0,
                        self.MAXX,
                        right_pos,
                        right_pos - left_pos
                    )

                # Remove obstacle from set
                obstacles.remove(x)

        # Reverse answers because queries were processed backwards
        return ans[::-1]