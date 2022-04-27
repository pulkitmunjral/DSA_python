def maxWindowSum(array, k):

    maxSum = 0
    windowSum = 0
    start = 0
    for i in range(len(array)):

        windowSum += array[i]
        if i >= k-1:
            maxSum = windowSum if windowSum > maxSum else maxSum
            windowSum -= array[start]
            start += 1
    return maxSum


ar = [8, 2, 4, 3, 7, 5]

print(maxWindowSum(ar,3))
