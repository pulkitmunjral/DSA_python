# to find the max product of the countinuos sub array


def maxProduct(array):
    res = max(array)
    currentMax, currentMin = 1, 1

    for n in array:

        if n == 0:
            currentMax, currentMin = 1, 1

        temp = currentMax

        currentMax = max(n*currentMax, n*currentMin, n)
        currentMin = min(temp*n, n*currentMin, n)
        res = max(res, currentMax)
        print(currentMax, currentMin, res)

    return res

print(maxProduct([2, 3, -2, 4, -1]))