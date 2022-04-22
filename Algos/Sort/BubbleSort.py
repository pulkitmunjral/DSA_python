# also called sinking sort
# compare adjacent element pushing largest to last
# use flag to keep track of the swaps in last iterations
# if no swaps make keep flag true and break which means array is already sorted


def BubbleSort(arr):
    lenght = len(arr)-1
    for i in range(lenght):
        flag = True
        for j in range(0, lenght):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]
                flag = False
        if flag:
            break
    return arr


arr = [5, 1, 9, 2, 10]
print(BubbleSort(arr))
