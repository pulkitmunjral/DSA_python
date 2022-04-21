class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def levelOrder(current):
    if current:
        queue = []
        queue.append(current)
        while len(queue) > 0:
            temp = queue.pop(0)
            print(temp.value)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
    else:
        return


def insertNode(root, value):
    if root:

        if root.value < value:
            root.right = insertNode(root.right, value)
        else:
            root.left = insertNode(root.left, value)

        return root
    else:
        root = Node(value)
        return root


def search(root, value):
    if not root or root.value==value:
        return True if root else False
    if value<root.value:
        return search(root.left, value)
    else:
        return search(root.right, value)


def checkTree(root, min, max):
    if not root:
        return True
    if root.value <= min or root.value >= max:
        return False

    left = checkTree(root.left, min, root.value)

    if left:
        right = checkTree(root.right, root.value, max)
        return right
    return False


root = Node(2)
insertNode(root,1)
insertNode(root,4)
insertNode(root,3)
insertNode(root,5)
insertNode(root,6)
insertNode(root,7)
# root.left.left= Node(10)
levelOrder(root)

print(checkTree(root, -10**5, 10**5))
