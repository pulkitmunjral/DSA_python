# find n numbers in binary with queue
n = 5

queue = ['1']

for i in range(5):
    temp = queue.pop(0)
    print(temp)
    queue.append(temp+'0')
    queue.append(temp+'1')
print(queue)