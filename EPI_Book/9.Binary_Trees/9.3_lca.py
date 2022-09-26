'''
find the lowest common ancestor
'''

from tree_traversal import BinaryTreeNode

def lca(self, root, p, q):

    #base cases
    if root == p or root == q:
        return root

    left = right = None
    if root.left:
        left = self.lca(root.left, p, q)
    if root.right:
        right = self.lca(root.right, p, q)
    
    if left and right:
        return root #this is the lca if both children returned nodes

    else:
        return left or right # either one of the node is below the node and we dont need to search all the way
