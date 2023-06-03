# You need to construct a binary tree from a string consisting of parenthesis and integers.

# The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. 
# The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if(root == None):
            return ""
        
        output: str = str(root.val)
        
        if (root.left != None or root.right != None):
            output += "(" + self.tree2str(root.left) + ")"
            
        if (root.right != None):
            output += "(" + self.tree2str(root.right) + ")"          
        
        return output;  
