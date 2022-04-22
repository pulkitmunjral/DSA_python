def insertionSort(array):

    for i in range(1, len(array)):
        temp = array[i]
        j = i-1

        while j >= 0 and array[j] > temp:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = temp

    return array


arr = [5, 1, 9, 2, 10]
print(insertionSort(arr))