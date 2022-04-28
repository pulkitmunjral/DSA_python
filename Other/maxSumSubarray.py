# to calculate maximum sum of a continuous sub array


def maxSumSubarray(array):

    maxSoFar = array[0]
    currentMax = array[0]

    for i in range(1, len(array)):
        currentMax = currentMax + array[i]
        if currentMax < array[i]:
            currentMax = array[i]
        if maxSoFar < currentMax:
            maxSoFar = currentMax

    return maxSoFar


ar = [4, 3, -2, 6, -12, 7, -1, 6]
print(maxSumSubarray(ar))
