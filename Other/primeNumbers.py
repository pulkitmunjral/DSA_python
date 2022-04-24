# remove all the tables

def getSumOfNPrimeNumebrs(n):
    prime = [1]*100003
    for i in range(2, len(prime)):
        if prime[i] == 1:
            for j in range(i+i, 100003, i):
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


