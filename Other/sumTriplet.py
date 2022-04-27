def sumOfTriplet(array, target):

    array.sort()
    ans = []
    for i in range(len(array)-2):

        j = i+1
        k = len(array)-1

        while j < k:
            su = array[i] + array[j] + array[k]
            if su == target:
                ans.append([array[i], array[j], array[k]])
                j += 1
                k -= 1
            elif su < target:
                j += 1
            else:
                k -= 1
    return ans


ar = [0, 1, 2, 3, 4, 7]
tar = 6
print(sumOfTriplet(ar, tar))