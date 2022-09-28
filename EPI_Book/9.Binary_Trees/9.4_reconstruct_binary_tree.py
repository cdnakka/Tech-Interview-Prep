'''
reconstruct binary tree given preorder and inorder traversal
'''
from tree_traversal import BinaryTreeNode

from typing import List
def buildtree(self, preorder: List[int], inorder:List[int]) -> BinaryTreeNode:
    if not preorder or not inorder:
        return None

    root = BinaryTreeNode(preorder[0])
    mid = inorder.index[preorder[0]]
    root.left = self.buildtree(preorder[1:mid+1], inorder[:mid])
    root.right = self.buildtree(preorder[mid+1:], inorder[mid+1:])
    return root


