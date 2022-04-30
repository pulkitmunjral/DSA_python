from queue import PriorityQueue
q = PriorityQueue()

q.put(1)
q.put(3)
q.put(2)

while not q.empty():
    print(q.get())


q = PriorityQueue()

q.put((1, 'z'))
q.put((3, 'r'))
q.put((2, 'z'))

while not q.empty():
    print(q.get())

