# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
#if there is no root then there can't be any depth
        if not root:
            return 0
#if the node has no left node and no right node, then it means it is the leaf node.

#first of make the double valued queue to keep the track of nodes and heights simultaniously. DEQUE stands for "double-ended queue".
# set deque with root node and height 1
 
        queue = deque([(root, 1)])

# as long as the queue is not empty, we will keep checking
        while queue:
            node, depth = queue.popleft()
#remove the first node and see if it has any child or not, 
            if not node.left and not node.right:
                return depth
#incase of any child,add that child in the queue and move on to increase the depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return depth