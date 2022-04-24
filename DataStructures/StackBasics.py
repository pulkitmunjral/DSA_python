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


# find first bigger node on the right
arr = [4, 7, 3, 4, 8, 1]
l = len(arr)
ans = [0]*l
stack = []

for i in range(l-1, -1, -1):
    n_stack = len(stack)
    while n_stack > 0 and stack[-1] <= arr[i]:
        stack.pop()
        n_stack = len(stack)

    if n_stack == 0:
        ans[i] = -1
    else:
        ans[i] = stack[-1]
    stack.append(arr[i])

print(ans)
