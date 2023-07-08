# Q1.Given preorder of a binary tree, calculate its **[depth(or height)]
# (https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/)**
# [starting from depth 0]. The preorder is given as a string with two possible characters.

# 1. ‘l’ denotes the leaf
# 2. ‘n’ denotes internal node

# The given tree can be seen as a full binary tree where every node has 0 or 
# two children. The two children of a node can ‘n’ or ‘l’ or mix of both.

def calculateTreeDepth(preorder):
    depth = 0
    max_depth = 0

    for char in preorder:
        if char == 'n':
            depth += 1
            max_depth = max(max_depth, depth)
        elif char == 'l':
            depth -= 1

    return max_depth


# Example usage
preorder = "nlnll"
depth = calculateTreeDepth(preorder)
print(depth)  # Output: 2




# Q2. Given a Binary tree, the task is to print the left view of the Binary Tree.
# The left view of a Binary Tree is a set of leftmost nodes for every level.


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def printLeftView(root):
    if root is None:
        return

    queue = [(root, 1)]  # Use a queue to perform level-order traversal

    # Initialize variables to track the current level and the leftmost node at each level
    current_level = 0
    leftmost_node = None

    while queue:
        node, level = queue.pop(0)

        if level > current_level:
            # A new level is encountered, print the leftmost node of the previous level
            if leftmost_node is not None:
                print(leftmost_node.val, end=" ")
            current_level = level

        # Update the leftmost node at the current level
        if level == 1:
            leftmost_node = node

        # Add the left and right children to the queue
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    # Print the leftmost node of the last level
    if leftmost_node is not None:
        print(leftmost_node.val)


# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)
root.right.left.right = TreeNode(8)

# Print the left view of the binary tree
printLeftView(root)

# Output: 1 2 4 7


# Q3. Given a Binary Tree, print the Right view of it.

# The right view of a Binary Tree is a set of nodes visible when the tree is visited from the Right side.


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def printRightView(root):
    if root is None:
        return

    queue = [(root, 1)]  # Use a queue to perform level-order traversal

    # Initialize variables to track the current level and the rightmost node at each level
    current_level = 0
    rightmost_node = None

    while queue:
        node, level = queue.pop(0)

        if level > current_level:
            # A new level is encountered, print the rightmost node of the previous level
            if rightmost_node is not None:
                print(rightmost_node.val, end=" ")
            current_level = level

        # Update the rightmost node at the current level
        rightmost_node = node

        # Add the left and right children to the queue
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    # Print the rightmost node of the last level
    if rightmost_node is not None:
        print(rightmost_node.val)


# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)
root.right.left.right = TreeNode(8)

# Print the right view of the binary tree
printRightView(root)

# Output: 1 3 6 8

# Q4. Given a Binary Tree, The task is to print the bottom view from left to right.
# A node x is there in output if x is the bottommost node at its horizontal distance.
# The horizontal distance of the left child of a node x is equal to a horizontal 
# distance of x minus 1, and that of a right child is the horizontal distance of x plus 1.

from collections import deque

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class NodeInfo:
    def __init__(self, node, hd):
        self.node = node
        self.hd = hd


def printBottomView(root):
    if root is None:
        return

    # Dictionary to store the bottommost node at each horizontal distance
    bottom_view = {}

    # Perform a vertical order traversal using a queue
    queue = deque()
    queue.append(NodeInfo(root, 0))

    while queue:
        node_info = queue.popleft()
        node = node_info.node
        hd = node_info.hd

        # Update the bottom view dictionary with the current node
        bottom_view[hd] = node.val

        # Enqueue the left and right children with updated horizontal distances
        if node.left:
            queue.append(NodeInfo(node.left, hd - 1))
        if node.right:
            queue.append(NodeInfo(node.right, hd + 1))

    # Print the bottom view from left to right
    for hd in sorted(bottom_view.keys()):
        print(bottom_view[hd], end=" ")

# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)
root.right.left.right = TreeNode(8)

# Print the bottom view of the binary tree
printBottomView(root)

# Output: 7 2 5 6 8


