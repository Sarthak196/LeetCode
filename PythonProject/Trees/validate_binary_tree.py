class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isValidBST(self, root):
        def validate(node, low, high):
            if node is None:
                return True
            if node.val <= low or node.val >= high:
                return False
            return(
                validate(node.left, low, node.val) # left value should not be greater than it's parent's val and higher than -inf
                and
                validate(node.right, node.val, high) # right value should not be less than it's parent's val and lower than inf
            )
        validate(root, float("-inf"), float("inf"))