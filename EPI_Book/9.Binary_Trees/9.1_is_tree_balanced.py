'''
Height balanced binary tree when the difference of heights between left and right subtrees is atmost 1
'''

from tree_traversal import BinaryTreeNode

def isBalanced(root):

    #set base root value as 1
    if root is None: 
        return True

    #recursive steps
    lh = isBalanced(root.left)
    #returns height if balanced, Flag if not balanced
    if lh == -1:
        return -1

    rh = isBalanced(root.right)
    if rh == -1 :
        return -1

    if abs(lh -rh) > 1 :
        return -1

    # If we reach here means tree is
    # height-balanced tree, return height
    # in this case
    else: 
        return(max(lh, rh) + 1)


# Driver code
if __name__ == '__main__':
    root = BinaryTreeNode(10)
    root.left = BinaryTreeNode(5)
    root.right = BinaryTreeNode(30)
    root.right.left = BinaryTreeNode(15)
    root.right.right = BinaryTreeNode(20)
    if (isBalanced(root) == -1):
        print("Not Balanced")
    else:
        print("Balanced")