# with hash map do sum of 2 elements matching to the target and return there index

class hashMap():

    def __init__(self, size):
        self.size = size
        self.hashTree = [[] for _ in range(size)]

    def set_val(self, key, value):
        bucket, i = self.find(key)
        if i != -1:
            bucket[i] = (key, value)
        else:
            bucket.append((key, value))

    def get_val(self, key):
        bucket, i = self.find(key)
        return bucket[i][1] if i != -1 else i


    def find(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hashTree[hashed_key]
        index = 0
        for index, record in enumerate(bucket):
            record_key, record_value = record

            if key == record_key:
                return bucket, index
        return bucket, -1



def findIndex(array, target):
    l = len(array)
    tree = hashMap(l)
    for i in range(l):
        sub = target-array[i]
        index = tree.get_val(sub)
        if index != -1:
            return [index, i]
        else:
            tree.set_val(array[i], i)
    return "Not possible"



def find(array, target):

    hashMap = {}
    ans = []
    for i in range(len(array)):
        if array[i] in hashMap:
            hashMap[array[i]] += 1
        else:
            hashMap[array[i]] = 1

        sub = target - array[i]
        if sub not in hashMap:
            continue

        if sub == array[i]:

            if hashMap[array[i]] > 1:
                ans.append((array[i], array[i]))
                hashMap[array[i]] -= 2
        else:

            if hashMap[array[i]] > 0 and hashMap[sub] > 0:
                ans.append((array[i], sub))

                hashMap[array[i]] -= 1

                hashMap[sub] -= 1

    return ans if ans else [(-1, -1)]


array = [2, 11, 5, 10, 7, 8, 1]
print(find(array, 9))

