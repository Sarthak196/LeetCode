class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def lowestCommonAncestor(self, root, p, q):
        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: # Both sides found something: The current node is the LCA, so return root
            return root
        return left or right # Only one side found something: Propagate that result upward using left or right