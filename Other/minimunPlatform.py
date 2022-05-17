"""Given arrival and departure times of all trains that reach a railway station.
Find the minimum number of platforms required for the railway station so that no train is kept waiting.
Consider that all the trains arrive on the same day and leave on the same day.
Arrival and departure time can never be the same for a train but we can have arrival time of one train equal
to departure time of the other. At any given instance of time, same platform can not be used for both departure
of a train and arrival of another train. In such cases, we need different platforms.
Input: n = 6
arr[] = {0900, 0940, 0950, 1100, 1500, 1800}
dep[] = {0910, 1200, 1120, 1130, 1900, 2000}
Output: 3
Explanation:
Minimum 3 platforms are required to
safely arrive and depart all trains.
  """

# for time to be n and space to be 1
def min(n,arr,dep):

    plat = [0 for _ in range(2401)]
    for i in range(n):
        plat[arr[i]] += 1
        plat[dep[i]+1] -= 1
    ans = 1
    for i in range(1, 2400):
        plat[i] += plat[i-1]
        ans = max(ans, plat[i])
    print(ans)


# time nlongn and space n
def minimumPlatform( n, arr, dep):
    # code here
    arr.sort()
    dep.sort()

    platforms = 1
    minPlatforms = 0
    i = 1
    j = 0
    while i < n and j < n:
        if arr[i] <= dep[j]:
            i += 1
            platforms += 1
        else:
            j += 1
            platforms -= 1
        minPlatforms = max(minPlatforms, platforms)

    print(minPlatforms)


minimumPlatform(6,[900, 940, 950, 1100, 1500, 1800],[910, 1200, 1120, 1130, 1900, 2000])
min(6,[900, 940, 950, 1100, 1500, 1800],[910, 1200, 1120, 1130, 1900, 2000])