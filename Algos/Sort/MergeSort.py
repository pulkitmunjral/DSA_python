def merge(array, low, mid, high):
    array_1 = array[low:mid+1]
    array_2 = array[mid+1:high+1]
    i = 0
    j = 0
    n = len(array_1)
    m = len(array_2)
    k = low
    while i < n and j < m:
        if array_1[i] < array_2[j]:
            array[k]=array_1[i]
            i += 1
        else:
            array[k] = array_2[j]
            j += 1
        k+=1

    while i < n:
        array[k] = array_1[i]
        i += 1
        k+=1
    while j < m:
        array[k] = array_2[j]
        j += 1
        k+=1



def Sort(array, low, high):
    if low < high:
        mid = (low + high)//2
        Sort(array, low, mid)
        Sort(array, mid+1, high)
        merge(array, low, mid, high)


arr = [2, -1, 6, 8, 1, 3]
Sort(arr,0,len(arr))
print(arr)


