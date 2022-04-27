# rearrange the sorted without using new array
# with help of mathematical formula save both values in 1 location

def maxminpattern(array):
    k = 0
    j = len(array)-1
    max = array[-1]+1

    for i in range(len(array)):
        if i % 2 == 0:
            array[i] = array[i] + (array[j] % max)*max
            j -= 1
        else:
            array[i] = array[i] + (array[k] % max)*max
            k += 1
    for i in range(len(array)):
        array[i] //= max


ar = [1, 2, 3, 5, 6, 9]
maxminpattern(ar)
print(ar)
