# remove all the tables

def getSumOfNPrimeNumebrs(n):
    till = 100003
    prime = [1]*till
    for i in range(2, int(till**0.5)+1):
        if prime[i] == 1:
            for j in range(i*i, till, i):
                prime[j] = 0

    ans = 0
    i = 1

    while n > 0 and i < 100003:
        if prime[i] == 1:
            ans += i
            n -= 1
        i += 1
    return ans

print(getSumOfNPrimeNumebrs(4))


