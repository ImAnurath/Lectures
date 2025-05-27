# LAB2
import random
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root: # No root? Make one
            self.root = Node(value)
        else:
            self._insert(value, self.root) # Yes root? Sudo insert 

    def _insert(self, value, node): # If there is a root invoke
        if value < node.value: # Less than the node? Go left
            if not node.left: # if left is empty
                node.left = Node(value)
            else:
                self._insert(value, node.left)
        else: # Greater than the node? Go right
            if not node.right: # if no right
                node.right = Node(value)
            else:
                self._insert(value, node.right)
random.seed(69)
random_nums = [random.randint(0,100) for _ in range(10)]
print(random_nums)
tree = BinaryTree()
for num in random_nums:
    tree.insert(num)
def traverse(node, above=None, left_or_right=None):
    if node is None:
        return
    if above is not None:
        print(f"{node.value} is {'left' if left_or_right == 'left' else 'right'} child of {above.value}")
    else:
        print(f"{node.value}")
    traverse(node.left, node, 'left')
    traverse(node.right, node, 'right')

traverse(tree.root)
def search(node, value, parent=None, direction=None):
    if node is None:
        print(f"{value} is not in the tree")
        return None
    if node.value == value:
        if parent is not None:
            print(f"Found {value}, which is a {'left' if direction == 'left' else 'right'} child of {parent.value}")
        else:
            print(f"Found {value}, which is the root")
        return node
    if value < node.value:
        return search(node.left, value, node, 'left')
    return search(node.right, value, node, 'right')
search(tree.root, 44)
#AV