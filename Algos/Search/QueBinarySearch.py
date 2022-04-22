# Add an element in the sorted array by log(n) and return it's index
# if the element is found return the index of that element which means new element will go on that index only
# if element is not found then due to while loop low will become low>high
# at this point our element will be stored at low


def AddElement(list, value):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low+high)//2
        mid_value = list[mid]
        if mid_value == value:
            return mid
        if value < mid_value:
            high = mid - 1
        else:
            low = mid + 1

    return low


a = [1,2,4,5]

print(AddElement(a,3))
print(AddElement(a,2))
print(AddElement(a,8))