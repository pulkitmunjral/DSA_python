#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.lru = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.lru:
            return -1
        else:
            self.lru.move_to_end(key)
            return self.lru[key]


    def put(self, key: int, value: int) -> None:
        self.lru[key] = value
        self.lru.move_to_end(key)
        if len(self.lru)>self.size:
            self.lru.popitem( last= False )


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

