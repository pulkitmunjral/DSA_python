#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0

        prime = [1]*n

        for i in range(2,int(n**0.5)+1):
            if prime[i]==1:
                for j in range(i*i,n,i):
                    prime[j]=0

        return sum(prime)-2

        
# @lc code=end

