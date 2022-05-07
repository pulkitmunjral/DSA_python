#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            ans = collections.defaultdict(list)
            # logic 1 O(NKlogK)
            for s in strs:
                ans[tuple(sorted(s))].append(s)

            # logic 2 O(NK)
            # for s in strs:
            #     count = [0] * 26
            #     for c in s:
            #         count[ord(c) - ord('a')] += 1
            #     ans[tuple(count)].append(s)
            return ans.values()
# @lc code=end

