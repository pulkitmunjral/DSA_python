arr = [4, 7, 3, 4, 8, 1]
l = len(arr)
ans = [0]*l
stack = []

# find first bigger node on the right
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


ans = [0]*l
stack = []
# find first bigger node on the left
for i in range(l):
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
