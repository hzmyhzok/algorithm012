# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder: 
            return
        root = TreeNode(preorder[0])
        id = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1 + id], inorder[:id])
        root.right = self.buildTree(preorder[1 + id:], inorder[id + 1:])
        return root