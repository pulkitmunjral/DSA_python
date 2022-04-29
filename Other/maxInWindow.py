# to find the maximum element in the window
# we can iterate on

from datetime import datetime
start_time = datetime.now()

def biggerElementRight(array):

    stack = []
    size = len(array)
    ans = [0]*size
    for i in range(size-1, -1, -1):

        while stack and array[i]>array[stack[-1]]:
            stack.pop()

        if not stack:
            ans[i] = size
        else:
            ans[i] = stack[-1]
        stack.append(i)

    return ans


def maxWindow(array, windowSize):

    temp = biggerElementRight(array)
    ans = []
    for i in range(len(array) - windowSize + 1):
        j = i

        while temp[j] < i + windowSize:
            j = temp[j]
        ans.append(array[j])

    return ans




array = [44, 77, 33, 44, 88, 11]
windowSize = 3

print(maxWindow(array, windowSize))
print('Duration: {}'.format(datetime.now() - start_time))
ans = [77, 77, 88, 88]