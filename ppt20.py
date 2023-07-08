# Q1.Given a binary tree, your task is to find subtree with maximum sum in tree.

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def findMaxSubtreeSum(root):
    max_sum = float('-inf')  # Initialize max_sum as negative infinity
    max_sum_subtree = None  # Initialize max_sum_subtree as None

    def subtreeSum(node):
        nonlocal max_sum, max_sum_subtree

        if node is None:
            return 0

        # Calculate sum of left and right subtrees recursively
        left_sum = subtreeSum(node.left)
        right_sum = subtreeSum(node.right)

        # Calculate sum of current subtree
        subtree_sum = left_sum + right_sum + node.val

        # Update max_sum and max_sum_subtree if current subtree has higher sum
        if subtree_sum > max_sum:
            max_sum = subtree_sum
            max_sum_subtree = node

        # Return sum of current subtree
        return subtree_sum

    # Call the helper function to traverse the binary tree
    subtreeSum(root)

    return max_sum_subtree


# Q2.Construct the BST (Binary Search Tree) from its given level order traversal.

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def constructBST(level_order):
    if not level_order:
        return None

    root = TreeNode(level_order[0])
    queue = [root]
    i = 1

    while queue and i < len(level_order):
        node = queue.pop(0)

        # Create left child
        if level_order[i] is not None:
            node.left = TreeNode(level_order[i])
            queue.append(node.left)
        i += 1

        # Create right child
        if i < len(level_order) and level_order[i] is not None:
            node.right = TreeNode(level_order[i])
            queue.append(node.right)
        i += 1

    return root


level_order = [5, 3, 8, 2, 4, None, 9, 1, None, None, None, 6, None, None, 7]
root = constructBST(level_order)
eg:-
#       5
#      / \
#     3   8
#    / \   \
#   2   4   9
#  /       /
# 1       6
#        /
#       7


# Q3. Given an array of size n. The problem is to check whether the given 
# array can represent the level order traversal of a Binary Search Tree or not.

def canRepresentBSTLevelOrder(arr):
    if not arr:
        return True

    n = len(arr)
    i = 1

    while i < n:
        if arr[i] < arr[0]:
            i += 1
        else:
            break

    for j in range(i, n):
        if arr[j] < arr[0]:
            return False

    left_subtree = True
    if i > 1:
        left_subtree = canRepresentBSTLevelOrder(arr[1:i])

    right_subtree = True
    if i < n:
        right_subtree = canRepresentBSTLevelOrder(arr[i:])

    return left_subtree and right_subtree



level_order = [7, 4, 12, 3, 6, 8, 1, 5, 10]
result = canRepresentBSTLevelOrder(level_order)
print(result)  # Output: True







