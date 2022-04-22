def mergeArray(array_1, array_2):
    i = 0
    j = 0
    n = len(array_1)
    m = len(array_2)
    ans = []

    while i < n and j < m:
        if array_1[i] < array_2[j]:
            ans.append(array_1[i])
            i += 1
        else:
            ans.append(array_2[j])
            j += 1

    while i < n:
        ans.append(array_1[i])
        i += 1
    while j < m:
        ans.append(array_2[j])
        j += 1

    return ans


arr_1 = [2, 5, 11]
arr_2 = [3, 4, 9, 10]

print(mergeArray(arr_1, arr_2))
