from queue import PriorityQueue
q = PriorityQueue()

q.put(1)
q.put(1)
q.put(2)
print(q.queue)
while not q.empty():
    print(q.get())


q = PriorityQueue()

q.put((1, 'z'))
q.put((1, 'r'))
q.put((2, 'z'))

while not q.empty():
    print(q.get())

