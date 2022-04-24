arr = [3,0,2,5,2,1,2,6,4]

l = len(arr)

left_arr = [0]*l
right_arr = [0]*l

for i in range(l-2, -1, -1):
    current_element = arr[i]
    if current_element >= arr[i+1]:
        left_arr[i] = 1 + left_arr[i+1]

for i in range(1, l):
    current_element = arr[i]
    if current_element >= arr[i-1]:
        right_arr[i] = 1 + right_arr[i-1]

ans = []
for i in range(l):
    ans.append(left_arr[i]+right_arr[i])

print("Longest width of the hill", max(ans)+1)
print("Index of the peak of hill", ans.index(max(ans)))