# Queue represented by list
Queue = []

# To enqueue data use append()
Queue.append(10)
Queue.append(20)
Queue.append(30)
print(f"Queue after enqueue operation {Queue}")

# to dequeue data use pop() function
print(f"dequeue vale is {Queue.pop(0)}")
print(f"Queue after dequeue operation {Queue}")

# to see top element
print(f"top element {Queue[0]}")

# to see rear element
print(f"rear element {Queue[-1]}")

# empty queue
print(len(Queue)==0)