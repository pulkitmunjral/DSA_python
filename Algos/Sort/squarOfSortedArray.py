# on squaring -ve numbers become +ve so if square a sorted list then there is a need of sorting them again
# which will take n + nLog(n) time  O(nlog(n))
# this algo will give the ans in O(n)

def squareOfSortedArray(array):

    i = 0
    j = len(array)-1
    result = [0]*(j+1)
    for k in range(len(array)-1, -1, -1):
        if abs(array[i])>abs(array[j]):
            result[k] = array[i]**2
            i+=1
        else:
            result[k] = array[j]**2
            j-=1
    return result


arr = [-4, -1, 0, 2, 4]

print(squareOfSortedArray(arr))

