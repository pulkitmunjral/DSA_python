# choosing a element as pivot then moving all other small elements to it's left and larger to right
# then running same on just unsorted left and right parts, leaving pivot elements un touched


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i+1


def sort(array, low, high):
    if low < high:
        p = partition(array, low, high)
        sort(array, low, p-1)
        sort(array, p+1, high)


arr = [2, -1, 6, 8, 1, 3]
sort(arr, 0, len(arr)-1)
print(arr)
