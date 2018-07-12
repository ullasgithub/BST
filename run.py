from node import Node
from insert_node import insert
from  print_inorder_bst import inorder


if __name__ == '__main__':
    r = Node(50)
    insert(r, Node(30))
    insert(r, Node(20))
    insert(r, Node(40))
    insert(r, Node(70))
    insert(r, Node(60))
    insert(r, Node(80))
    # Print inorder traversal of the BST
    print("inorder treversal of the BST ")
    inorder(r)