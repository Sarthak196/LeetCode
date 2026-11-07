class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def kthSmallest(self, root, k):
        count = 0
        ans = None
        def inorder(node): # use inorder as that displays the tree in ascending order
            nonlocal ans, count
            if node is None or ans is not None: # recurse until ans is not found
                return
            inorder(node.left)
            count+=1 # as the left-est node is the smallest one increment the count
            if count == k:
                ans = node.val # as soon as answer is available return it so that ans will become not None and the base case will return ans
                return
            inorder(node.right)
        inorder(root)
        return ans