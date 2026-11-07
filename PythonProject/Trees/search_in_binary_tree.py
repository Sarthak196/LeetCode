class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def searchBST(self, root, val):
        if root is None or root.val == val:
            return root
        if root.val < val:
            return self.searchBST(root.right, val)
        return self.searchBST(root.left, val)