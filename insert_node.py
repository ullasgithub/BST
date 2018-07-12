def insert(root, node):
    if root is None:
        self.root = node
    else:
        if root.data < node.data:
            if root.right == None:
                root.right =node
            else:
                insert(root.right, node)
        else:
            if root.left == None:
                root.left =node
            else:
                insert(root.left, node)