# Print the element which is visible from left view
# we can keep track of level and print the first element of that level
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


global maxLevel
maxLevel = -1


def leftViewTree(root, level):

    global maxLevel
    if not root:
        return

    if level > maxLevel:
        print(root.value)
        maxLevel = level

    leftViewTree(root.left, level+1)
    leftViewTree(root.right, level+1)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(5)


leftViewTree(root, 0)
