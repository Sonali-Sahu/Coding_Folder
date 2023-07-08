# Q1.You are given a binary tree. The binary tree is represented using the
# TreeNode class. Each TreeNode has an integer value and left and right children,
# represented using the TreeNode class itself. Convert this binary tree into a binary search tree.

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def convertToBST(root):
    # Perform in-order traversal to get sorted values
    def inOrderTraversal(node):
        nonlocal values
        if node is None:
            return
        inOrderTraversal(node.left)
        values.append(node.val)
        inOrderTraversal(node.right)

    # Create new binary search tree using sorted values
    def createBST(values):
        if not values:
            return None

        mid = len(values) // 2
        root = TreeNode(values[mid])
        root.left = createBST(values[:mid])
        root.right = createBST(values[mid + 1:])
        return root

    # Perform in-order traversal to get sorted values
    values = []
    inOrderTraversal(root)

    # Create and return new binary search tree
    return createBST(values)


# Create a binary tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)

# Convert the binary tree to binary search tree
bst_root = convertToBST(root)

# Test the converted binary search tree
# Perform in-order traversal to check if the values are sorted
def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.val)
    inOrderTraversal(node.right)

inOrderTraversal(bst_root)



# Q2. Given a Binary Search Tree with all unique values and two keys. 
# Find the distance between two nodes in BST. The given keys always exist in BST.

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def findDistance(root, key1, key2):
    # Find the two nodes in the BST
    def findNodes(node, key1, key2):
        if node is None:
            return None

        if node.val == key1 or node.val == key2:
            return node

        left_result = findNodes(node.left, key1, key2)
        right_result = findNodes(node.right, key1, key2)

        if left_result and right_result:
            return node
        elif left_result:
            return left_result
        elif right_result:
            return right_result
        else:
            return None

    # Calculate the distance between a node and its ancestor
    def distanceToAncestor(node, key):
        if node.val == key:
            return 0

        if key < node.val:
            return 1 + distanceToAncestor(node.left, key)
        else:
            return 1 + distanceToAncestor(node.right, key)

    # Find the two nodes in the BST
    node1 = findNodes(root, key1, key2)
    node2 = node1.left if node1.val == key2 else node1.right

    # Calculate the distance between the two nodes
    distance1 = distanceToAncestor(node1, key2)
    distance2 = distanceToAncestor(node2, key1)

    return distance1 + distance2


# Create a Binary Search Tree
root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(10)

# Find the distance between two nodes in the BST
distance = findDistance(root, 2, 10)
print(distance)  # Output: 3


# Q3. Write a program to convert a binary tree to a doubly linked list.

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


def binaryTreeToDoublyLinkedList(root):
    # Helper function to perform in-order traversal and adjust pointers
    def convertToDoublyLinkedList(node):
        nonlocal prev, head

        if node is None:
            return

        # Recursively convert left subtree
        convertToDoublyLinkedList(node.left)

        # Create a new DoublyLinkedListNode for the current node
        curr = DoublyLinkedListNode(node.val)

        # Adjust the pointers
        if prev is None:
            head = curr
        else:
            prev.next = curr
            curr.prev = prev

        prev = curr

        # Recursively convert right subtree
        convertToDoublyLinkedList(node.right)

    prev = None  # Track the previous node
    head = None  # Head of the doubly linked list

    convertToDoublyLinkedList(root)

    return head


# Create a binary tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

# Convert binary tree to doubly linked list
doubly_linked_list_head = binaryTreeToDoublyLinkedList(root)

# Traverse the doubly linked list and print the values
current = doubly_linked_list_head
while current is not None:
    print(current.val, end=" ")
    current = current.next
  
# Q4. Write a program to connect nodes at the same level.

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.next = None


def connectNodesAtSameLevel(root):
    if root is None:
        return

    # Perform a level-order traversal
    queue = [root]

    while queue:
        level_size = len(queue)

        # Connect nodes at the same level
        for i in range(level_size):
            node = queue.pop(0)

            if i < level_size - 1:
                node.next = queue[0]

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return root


# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Connect nodes at the same level
connected_root = connectNodesAtSameLevel(root)

# Print the connected nodes at each level
current = connected_root
while current:
    level_start = current
    while current:
        print(current.val, end=" ")
        current = current.next
    print()  # Move to the next line for the next level
    current = level_start.left  # Move to the leftmost node of the next level


# Output:- 
# 1
# 2 3
# 4 5 6 7



















