# Stack represented by list
stack = []

# To push data use append()
stack.append(10)
stack.append(20)
stack.append(30)
print(f"stack after push operation {stack}")

# to pop data use pop() function
print(f"poped vale is {stack.pop()}")
print(f"stack after pop operation {stack}")

# to see top element
print(f"top element {stack[-1]}")

# empty Stack
print(len(stack)==0)
