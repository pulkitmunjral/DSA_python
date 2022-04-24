def merge(array, low, mid, high):

    array_1 = array[low:mid+1]
    array_2 = array[mid+1:high+1]

    len_array_1 = len(array_1)
    len_array_2 = len(array_2)

    iter_array_1 = 0
    iter_array_2 = 0
    iter_array = low

    while iter_array_1 < len_array_1 and iter_array_2 < len_array_2:

        if array_1[iter_array_1] < array_2[iter_array_2]:
            array[iter_array] = array_1[iter_array_1]
            iter_array_1 += 1

        else:
            array[iter_array] = array_2[iter_array_2]
            iter_array_2 += 1

        iter_array += 1

    while iter_array_1 < len_array_1:
        array[iter_array] = array_1[iter_array_1]
        iter_array_1 += 1
        iter_array += 1

    while iter_array_2 < len_array_2:
        array[iter_array] = array_2[iter_array_2]
        iter_array_2 += 1
        iter_array += 1


def sort(array, low, high):

    if low < high:

        mid = (low + high)//2

        sort(array, low, mid)
        sort(array, mid+1, high)
        merge(array, low, mid, high)


arr = [2, -1, 6, 8, 1, 3]
sort(arr,0,len(arr))
print(arr)