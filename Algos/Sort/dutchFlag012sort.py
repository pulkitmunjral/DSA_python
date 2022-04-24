# to move 0's at starting then 1's at middle then 2's at last position
# complexity O(n)

def dutchFlagSort(arr):
    i = 0    # just to iterate on elements of array
    j = 0     # to provide index space for 0 that is why starting from 0
    k = len(arr) - 1   # similarly index space for 2 that is why starting from end(len of arr -1 )

    while i <= k:

        if arr[i] == 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i], arr[k] = arr[k], arr[i]
            k -= 1
    return arr


arr = [1, 1, 0, 2, 1, 0]
print(dutchFlagSort(arr))
