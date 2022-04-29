# search ab element in 2d sorted array
# the array is sorted in its each row and in each column

def search(array, key):

    i = 0
    j = len(array[i])-1

    while i < len(array) and j < len(array[i]):
        current = array[i][j]
        if current == key:
            return [i, j]
        elif current > key:
            j -= 1
        else:
            i += 1
    return -1


array = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [27, 29, 37, 48],
    [32, 33, 39, 52]
]

print(search(array, 52))