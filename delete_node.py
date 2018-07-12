def minValueNode(node):
    current = node
    # loop down to find the leftmost leaf
    while (current.left is not None):
        current = current.left
    return current

def delete_node(root, data):
    # Base Case
    if root is None:
        return root

    # If the key to be deleted is smaller than the root's
    if data < root.data:
        root.left = delete_node(root.left, data)

    # If the kye to be delete is greater than the root's key
    elif (data > root.data):
        root.right = delete_node(root.right, data)

    # If key is same as root's key, then this is the node
    # to be deleted
    else:
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp
        # Node with two children: Get the inorder successor
        temp = minValueNode(root.right)
        # Copy the inorder successor's content to this node
        root.key = temp.key
        # Delete the inorder successor
        root.right = delete_node(root.right, temp.key)
    return root