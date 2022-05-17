"""Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
Note: Unlike 0/1 knapsack, you are allowed to break the item.
Input:
N = 3, W = 50
values[] = {60,100,120}
weight[] = {10,20,30}
Output:
240.00
Explanation:Total maximum value of item
we can have is 240.00 from the given
capacity of sack.

Input:
N = 2, W = 50
values[] = {60,100}
weight[] = {10,20}
Output:
160.00
Explanation:
Total maximum value of item
we can have is 160.00 from the given
capacity of sack.
"""


def fractionalknapsack( W, Items, n):
    Items = sorted(Items, reverse=True, key=lambda x: (x[0] / x[1]))
    amount = 0

    for item in Items:
        if W > item[1]:
            amount += item[0]
            W -= item[1]
        else:
            f = W / item[1]

            amount += item[0] * f
            break
    print(amount)

fractionalknapsack(50, [(60,10),(100,20),(120,30)], 3)