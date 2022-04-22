def selctionSort(array):

    lenght = len(array)-1
    for i in range(lenght):
        min = i
        for j in range(i+1, lenght+1):
            if array[j] < array[min]:
                min = j

        array[min], array[i] = array[i], array[min]

    return array


arr = [5, 1, 9, 2, 10]
print(selctionSort(arr))
