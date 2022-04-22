def BinarySearch(list, value):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low+high)//2
        mid_value = list[mid]
        if mid_value ==value:
            return mid
        if value < mid_value:
            high = mid - 1
        else:
            low = mid + 1

    return False

def BinarySearchRecusive(list, value, low, high):

    if low <= high:
        mid = (low+high)//2
        mid_value = list[mid]
        if mid_value == value:
            return mid
        if value < mid_value:
            return BinarySearchRecusive(list, value, low, mid - 1)
        else:
            return BinarySearchRecusive(list, value, mid + 1, high)
    else:
        return False

a = [1,2,3,4,5,6]

print(BinarySearchRecusive(a,50,0,len(a)-1))