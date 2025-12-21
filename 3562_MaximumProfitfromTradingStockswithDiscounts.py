class Solution(object):                     # Define a class named Solution

    def maxProfit(self, n, present, future, hierarchy, budget):  # Define function with inputs
        """
        :type n: int                         # Number of nodes
        :type present: List[int]             # Present cost of each node
        :type future: List[int]              # Future value of each node
        :type hierarchy: List[List[int]]     # Parent-child relationships
        :type budget: int                    # Maximum allowed budget
        :rtype: int                          # Return type is integer
        """

        from sys import setrecursionlimit     # Import function to change recursion depth
        setrecursionlimit(10**7)              # Allow deep recursion for DFS

        g = [[] for _ in range(n)]            # Create adjacency list for n nodes

        for u, v in hierarchy:                # Loop through hierarchy edges
            g[u-1].append(v-1)                # Add child v-1 to parent u-1

        def dfs(u):                           # Define DFS function for node u

            child_dp = [dfs(v) for v in g[u]] # Run DFS on all children and store their DP

            f0 = [float('-inf')] * (budget+1) # DP when parent of u is NOT chosen
            f1 = [float('-inf')] * (budget+1) # DP when parent of u IS chosen

            f0[0] = 0                         # Zero cost gives zero profit
            f1[0] = 0                         # Same for chosen parent case

            for dp_no_v, dp_yes_v in child_dp: # Loop through each child's DP result

                new0 = [float('-inf')] * (budget+1)  # New DP for f0
                new1 = [float('-inf')] * (budget+1)  # New DP for f1

                for spent in range(budget+1): # Loop through spent budget

                    if f0[spent] > -1e18:     # Check if state is valid
                        for k in range(budget-spent+1): # Budget used by child
                            val = f0[spent] + dp_no_v[k] # Add child profit
                            if val > new0[spent+k]:     # Take max
                                new0[spent+k] = val

                    if f1[spent] > -1e18:     # Check valid state
                        for k in range(budget-spent+1): # Budget used by child
                            val = f1[spent] + dp_yes_v[k] # Add child profit
                            if val > new1[spent+k]:     # Take max
                                new1[spent+k] = val

                f0, f1 = new0, new1           # Update DP after merging child

            dp_no_u = [float('-inf')] * (budget+1) # DP when u is NOT bought
            dp_yes_u = [float('-inf')] * (budget+1) # DP when u IS bought

            cost_no  = present[u]             # Cost without discount
            profit_no = future[u] - cost_no   # Profit without discount

            cost_yes  = present[u] // 2       # Cost with discount
            profit_yes = future[u] - cost_yes # Profit with discount

            for c in range(budget+1):         # Loop through budget

                if f0[c] > dp_no_u[c]:        # Skip buying u
                    dp_no_u[c] = f0[c]        # Store profit
                    dp_yes_u[c] = f0[c]       # Same for discounted path

                if c >= cost_no and f1[c-cost_no] + profit_no > dp_no_u[c]:
                    dp_no_u[c] = f1[c-cost_no] + profit_no # Buy u normally

                if c >= cost_yes and f1[c-cost_yes] + profit_yes > dp_yes_u[c]:
                    dp_yes_u[c] = f1[c-cost_yes] + profit_yes # Buy u with discount

            return dp_no_u, dp_yes_u           # Return DP arrays for node u

        dp_root_no, _ = dfs(0)                 # Run DFS from root node

        return max(dp_root_no[:budget+1])      # Return maximum profit within budget
