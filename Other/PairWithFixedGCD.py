# infosys find n numbers for which k is fixed gcd and there is sum is least return sum


def isPrime(j):
    for i in range(2, int(j**(1/2))+1):
        if j % i == 0:
            return False
    return True


def findSum(n, k):
    ans = 1
    j = 2
    mod = 10**9 + 7
    while n > 1:

        if isPrime(j):
            ans += j
            ans %= mod
            j += 1
            n -= 1
        else:
            j += 1

    return ans*k

print(findSum(3, 1))
