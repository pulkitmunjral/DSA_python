array = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [27, 29, 37, 48],
    [32, 33, 39, 52]
]

ans = [10, 20, 30, 40, 45, 48, 52, 39, 33, 32, 27, 15, 25, 35, 37, 29]

k = 0
l = 0
r = len(array)
c = len(array[0])


i = 0
while k < r and l < c:

    for i in range(l, c):
        print(array[k][i], end=" ")

    k += 1

    for i in range(k, r):
        print(array[i][c-1], end=" ")
    c -= 1

    if k < r:
        for i in range(c-1, l-1, -1):
            print(array[r-1][i], end=" ")
        r -= 1
    if l < c:
        for i in range(r-1, k-1, -1):
            print(array[i][l], end=" ")
        l += 1