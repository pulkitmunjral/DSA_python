# to count the frequency of char in the string
# then return the first non repeating char

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
        return bucket[i][1] if i != -1 else 0


    def find(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hashTree[hashed_key]

        for index, record in enumerate(bucket):
            record_key, record_value = record

            if key == record_key:
                return bucket, index
        return bucket, -1


def countFrequency(sub):

    tree = hashMap(len(sub))
    for i in sub:
        tree.set_val(i, tree.get_val(i)+1)

    for i in sub:
        if tree.get_val(i) == 1:
            return i

su = "abcabcdeddd"
print(countFrequency(su))