'''
common traversal techniques
'''
# from tree_traversal import BinaryTreeNode

class BinaryTreeNode:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def tree_traversal(root: BinaryTreeNode) -> None:
    if root:
        #preorder:
        print('PreOrder: %d' % root.data)
        tree_traversal(root.left)

        #inorder:
        print('InOrder %d' % root.data)
        tree_traversal(root.right)

        #postorder
        print("PostOrder %d" % root.data)

    
        