class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def diameterOfBinaryTree(self, root):
        diameter = 0
        def height(root):
            nonlocal diameter
            if root is None:
                return 0
            left_height = height(root.left)
            right_height = height(root.right)
            diameter = max(diameter, (left_height+right_height))
            return 1 + max(left_height, right_height)
        height(root)
        return diameter

t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)

print(t.diameterOfBinaryTree(t))