class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def preOrder(current):
    if current:
        print(current.value)
        preOrder(current.left)
        preOrder(current.right)

    else:
        return


def preOrder_stack(current):
    if current:
        stack = []
        stack.append(current)
        while len(stack)>0:
            temp = stack.pop()
            print(temp.value)
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
    else:
        return

def inOrder(current):
    if current:
        inOrder(current.left)
        print(current.value)
        inOrder(current.right)

    else:
        return


def postOrder(current):
    if current:
        postOrder(current.left)
        postOrder(current.right)
        print(current.value)

    else:
        return

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

def findMax(current):
    if current:
        result = current.value
        left = findMax(current.left)
        right = findMax(current.right)

        if left > result:
            result = left
        if right > result:
            result = right
        return result
    else:
        return -1


    """         1    
            2       3
        4       5       
    """

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(7)
root.right.left = Node(6)
print(findMax(root))
# preOrder_stack(root)