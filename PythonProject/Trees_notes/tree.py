class Tree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

    def insert_left(self, new_node):
        if self.left is None:
            self.left = Tree(new_node)
        else:
            new_tree = Tree(new_node)
            new_tree.left = self.left # new_tree's left child is the old left child
            self.left = new_tree # the left child of the current node is now the new tree

    def insert_right(self, new_node):
        if self.right is None:
            self.right = Tree(new_node)
        else:
            new_tree = Tree(new_node)
            new_tree.right = self.right # new_tree's right child is the old right child
            self.right = new_tree

    def get_left_child(self):
        return self.left.root

    def get_right_child(self):
        return self.right.root

    def get_root_value(self):
        return self.root

    def set_root_value(self, new_value):
        self.root = new_value

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.root)
        if self.right:
            self.right.inorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.root)

    def preorder_traversal(self):
        print(self.root)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()


t = Tree(1)
print(t.get_root_value()) # 1
t.insert_left(2)
t.insert_right(3)
t.insert_left(4)
t.insert_left(5)
print(t.get_left_child()) # 5
print(t.left.get_left_child()) # 4
print(t.left.left.get_left_child()) # 2
t.insert_right(6)
print(t.get_right_child()) # 6
print("Inorder Traversal:")
t.inorder_traversal()
print("Postorder Traversal:")
t.postorder_traversal()
print("Preorder Traversal:")
t.preorder_traversal()

       #        1
       #      /   \
       #     5     6
       #    /       \
       #   4         3
       #  /
       # 2