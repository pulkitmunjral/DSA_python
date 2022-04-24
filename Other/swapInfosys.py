array_1 = [1, 2]
array_2 = [1, 2]

i = 0
ans = 0
mod = 10**9 + 7
while array_2 != array_1:

    if array_1[i] == array_2[i]:
        i += 1
    else:
        ans += array_1[i] - array_1[i + 1]
        array_1[i], array_1[i+1] = array_1[i+1], array_1[i]
        i += 1
    if i == len(array_1):
        i = 0
    ans = ans % mod


print(ans)


