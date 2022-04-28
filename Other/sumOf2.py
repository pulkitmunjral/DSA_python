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


array = [2, 11, 5, 10, 7, 8]
print(findIndex(array, 9))

