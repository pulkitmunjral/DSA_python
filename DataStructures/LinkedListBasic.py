class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if not self.head:
            print("List is empty")
            return
        else:
            print("Element in list are")
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next
        print()
        return

    def findLoop(self):
        if not self.head:
            print("List is empty")
            return False
        else:
            slow = self.head
            fast = self.head
            while fast and fast.next :
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True
            return False


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        print("Node created")


# Initiate linkedlist
llist = LinkedList()
# llist.display()

# Created first node and saved it in head
llist.head = Node(10)

# creating new nodes
second = Node(20)
third = Node(30)
forth = Node(40)

# Linking each node to the linked list
llist.head.next = second

# # print linkedlist
# llist.display()

# linking few more nodes in last
second.next = third
third.next = forth
forth.next = second

# # printing complete linked list
# llist.display()

print(llist.findLoop())
