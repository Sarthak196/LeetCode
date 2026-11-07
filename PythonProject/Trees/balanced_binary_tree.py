class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isBalancednaryTree(self, root):
        def height(node):
            if node is None:
                return 0
            left_height = height(node.left)
            if left_height == -1:
                return -1
            right_height = height(node.right)
            if right_height == -1:
                return -1
            if abs(left_height - right_height) > 1: # a blanced binary tree will never have its node height > 1
                return -1
            return 1+ max(left_height, right_height)
        return height(root) != -1

#time complexity: O(n)