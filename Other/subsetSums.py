"""
Given a list arr of N integers, print sums of all subsets in it.
Input:
N = 2
arr[] = {2, 3}
Output:
0 2 3 5
Explanation:
When no elements is taken then Sum = 0.
When only 2 is taken then Sum = 2.
When only 3 is taken then Sum = 3.
When element 2 and 3 are taken then
Sum = 2+3 = 5.
Input:
N = 3
arr = {5, 2, 1}
Output:
0 1 2 3 5 6 7 8
"""


def subsetSums(arr, N):
    # code here
    ans = []

    def sub(arr, N, i=0, su=0):
        if i == N:
            ans.append(su)
            return
        print(i+1,su)
        print(i+1,su+arr[i])
        sub(arr, N, i + 1, su)
        sub(arr, N, i + 1, su + arr[i])


    sub(arr, N)
    return ans

print(subsetSums([2, 3],2))