def search(node, key):
    if node is None:
        return None  # key not found
    if key< node.data:
        return search(node.left, key)
    elif key> node.data:
        return search(node.right, key)
    else:
        return node.data  # found key