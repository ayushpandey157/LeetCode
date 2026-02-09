# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Inorder traversal to collect BST elements in sorted order
    def inorder(self, root, nodes):
        if not root:
            return
        self.inorder(root.left, nodes)
        nodes.append(root.val)
        self.inorder(root.right, nodes)

    # Build a height-balanced BST from sorted list
    def buildBST(self, left, right, nodes):
        if left > right:
            return None

        mid = (left + right) // 2  # choose middle element as root
        root = TreeNode(nodes[mid])

        # Recursively build left and right subtrees
        root.left = self.buildBST(left, mid - 1, nodes)
        root.right = self.buildBST(mid + 1, right, nodes)

        return root

    def balanceBST(self, root):
        nodes = []

        # Step 1: Store inorder traversal of BST
        self.inorder(root, nodes)

        # Step 2: Build balanced BST from sorted values
        return self.buildBST(0, len(nodes) - 1, nodes)