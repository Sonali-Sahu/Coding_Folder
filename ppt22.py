# Q1. Given a Binary Tree (Bt), convert it to a Doubly Linked List(DLL).
# The left and right pointers in nodes are to be used as previous and next pointers 
# respectively in converted DLL. The order of nodes in DLL must be the same as in Inorder
# for the given Binary Tree. The first node of Inorder traversal (leftmost node in BT)
# must be the head node of the DLL.

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class DoublyLinkedListNode:
    def __init__(self, value):
        self.val = value
        self.prev = None
        self.next = None


def convertBTtoDLL(root):
    if root is None:
        return None

    def convert(node):
        nonlocal prev

        if node is None:
            return

        # Convert left subtree
        convert(node.left)

        # Create a DoublyLinkedListNode for the current node
        current = DoublyLinkedListNode(node.val)

        # Adjust pointers
        if prev is None:
            head = current
        else:
            current.prev = prev
            prev.next = current

        prev = current

        # Convert right subtree
        convert(node.right)

    # Initialize prev as None
    prev = None

    # Convert the BT to DLL
    convert(root)

    # Find the head of the DLL
    head = prev
    while head and head.prev:
        head = head.prev

    return head


# Create a Binary Tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

# Convert Binary Tree to Doubly Linked List
dll_head = convertBTtoDLL(root)

# Traverse the Doubly Linked List forwards
current = dll_head
while current:
    print(current.val, end=" ")
    current = current.next

# Output: 1 2 3 4 5 6 7


# Q2. A Given a binary tree, the task is to flip the binary tree towards
# the right direction that is clockwise. See the below examples to see the transformation.

# In the flip operation, the leftmost node becomes the root of the flipped tree and 
# its parent becomes its right child and the right sibling becomes its left child and
# the same should be done for all left most nodes recursively.



class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def flipBinaryTree(root):
    # Base case: if the root is None or it is a leaf node
    if root is None or (root.left is None and root.right is None):
        return root

    flipped_left = flipBinaryTree(root.left)
    flipped_right = flipBinaryTree(root.right)

    # Flip the tree by swapping the left and right child pointers
    root.left = flipped_right
    root.right = flipped_left

    return root


# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Flip the binary tree clockwise
flipped_root = flipBinaryTree(root)

# Traverse the flipped binary tree in preorder to verify the transformation
def preorderTraversal(node):
    if node is None:
        return

    print(node.val, end=" ")
    preorderTraversal(node.left)
    preorderTraversal(node.right)

preorderTraversal(flipped_root)

# Output: 1 3 7 6 2 5 4


# Q3. Given a binary tree, print all its root-to-leaf paths without using recursion. For example, consider the following Binary Tree.

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def printRootToLeafPaths(root):
    if root is None:
        return

    # Create an empty stack to store the nodes and their paths
    stack = [(root, str(root.val))]

    while stack:
        node, path = stack.pop()

        if node.left is None and node.right is None:
            # Leaf node reached, print the path
            print(path)
        else:
            # Non-leaf node, continue traversing left and right subtrees
            if node.left:
                stack.append((node.left, path + " -> " + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + " -> " + str(node.right.val)))


# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Print all root-to-leaf paths
printRootToLeafPaths(root)

# Output:
# 1 -> 2 -> 4
# 1 -> 2 -> 5
# 1 -> 3 -> 6
# 1 -> 3 -> 7


# Q4. Given Preorder, Inorder and Postorder traversals of some tree. 
# Write a program to check if they all are of the same tree.




def checkSameTree(preorder, inorder, postorder):
    if len(preorder) != len(inorder) or len(preorder) != len(postorder):
        return False

    if len(preorder) == 0:
        return True

    root = preorder[0]
    preorder = preorder[1:]

    root_index = inorder.index(root)
    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1:]

    root_index = postorder.index(root)
    left_postorder = postorder[:root_index]
    right_postorder = postorder[root_index + 1 : -1]

    return (
        checkSameTree(preorder, left_inorder, left_postorder)
        and checkSameTree(preorder, right_inorder, right_postorder)
        and root == postorder[-1]
    )


# Example usage
preorder = [1, 2, 4, 5, 3]
inorder = [4, 2, 5, 1, 3]
postorder = [4, 5, 2, 3, 1]

result = checkSameTree(preorder, inorder, postorder)
print(result)  # Output: True

