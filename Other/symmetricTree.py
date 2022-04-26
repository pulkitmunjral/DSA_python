# to find if the tree is symmetric or a mirror image on placing mirror on root

def symmetricTree(tree):

    if not tree:
        return False
    stack = []
    stack.append(tree.left)
    stack.append(tree.right)

    while len(stack) > 0:
        n1 = stack.pop()
        n2 = stack.pop()

        if n1 is None and n2 is None:
            continue
        elif n1 is None or n2 is None or n1.value != n2.value:
            return False

        stack.append(n1.left)
        stack.append(n2.right)
        stack.append(n1.right)
        stack.append(n2.left)

    return True


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(4)
root.right.right = Node(4)

print(symmetricTree(root))