# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val      # value of the node
#         self.left = left    # reference to left child
#         self.right = right  # reference to right child

class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """

        # recursive function to build tree from a node value
        def construct_tree(cur_node_val):

            new_node = TreeNode(cur_node_val)  # create node

            # check if this node has children
            if cur_node_val in children_hashmap:

                # if left child exists, recursively build left subtree
                if children_hashmap[cur_node_val][0] is not None:
                    new_node.left = construct_tree(children_hashmap[cur_node_val][0])

                # if right child exists, recursively build right subtree
                if children_hashmap[cur_node_val][1] is not None:
                    new_node.right = construct_tree(children_hashmap[cur_node_val][1])

            return new_node  # return constructed subtree


        children_set = set()      # store all nodes that appear as children
        children_hashmap = {}     # parent -> [leftChild, rightChild]

        # process each description
        for parent, child, isleft in descriptions:

            # create entry for parent if not present
            if parent not in children_hashmap:
                children_hashmap[parent] = [None, None]  # [left, right]

            children_set.add(child)  # record child node

            # decide whether child is left or right
            target = 0 if isleft else 1

            # assign child to left or right position
            children_hashmap[parent][target] = child


        # find root (node that never appears as a child)
        for parent in children_hashmap:
            if parent not in children_set:
                head_node_val = parent
                break

        # construct tree starting from root
        head = construct_tree(head_node_val)

        return head  # return root of constructed tree