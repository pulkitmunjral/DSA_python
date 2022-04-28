# Print the element which is visible as a boundary like from left down to top root then to right down
# we can keep track of level and print the first element of that level
#             1
#         2       3
#     4      5  6    7
# output required 4 2 1 3 7

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def leftViewTree(root, level, li):

    global maxLevel
    if not root:
        return

    if level > maxLevel:
        li.append(root.value)
        maxLevel = level

    leftViewTree(root.left, level+1, li)


def rightViewTree(root, level, li):

    global maxLevel
    if not root:
        return

    if level > maxLevel:
        li.append(root.value)
        maxLevel = level

    rightViewTree(root.right, level+1, li)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(7)
root.right.left = Node(6)

global maxLevel
maxLevel = -1
li = []
leftViewTree(root.left, 0, li)
maxLevel = -1
li = li[::-1]
rightViewTree(root, 0, li)
print(li)