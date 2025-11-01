# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        
        def dfs(node):
            # if node is None, store "null"
            if not node:
                vals.append("null")
                return
            # store the node's value
            vals.append(str(node.val))
            # recursively visit left child
            dfs(node.left)
            # recursively visit right child
            dfs(node.right)
        
        vals = []  # list to hold serialized values
        dfs(root)  # start DFS from root
        return ",".join(vals)  # join values with commas into a string


    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        
        def dfs():
            # get next value from iterator
            val = next(vals)
            # if "null", return None (no node)
            if val == "null":
                return None
            # create a new TreeNode with the value
            node = TreeNode(int(val))
            # build left subtree
            node.left = dfs()
            # build right subtree
            node.right = dfs()
            # return the node
            return node
        
        vals = iter(data.split(","))  # split data into values and make iterator
        return dfs()  # reconstruct and return the root node


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
