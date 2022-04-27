# find product of list of element other than self without using division


def product(array):
    ans = []
    temp = 1
    for i in array:
        ans.append(temp)
        temp *= i

    temp = 1
    for j in range(len(array)-1, -1, -1):
        ans[j] *= temp
        temp *= array[j]
    return ans


arr = [-1, 1, 0, -3, 3]
print(product(arr))
