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
        return bucket[i][1] if i != -1 else "no data found"

    def del_val(self, key):
        bucket, i = self.find(key)
        return bucket.pop(i) if i != -1 else print("no data found")


    def find(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hashTree[hashed_key]
        index = 0
        for index, record in enumerate(bucket):
            record_key, record_value = record

            if key == record_key:
                return bucket, index
        return bucket, -1


    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hashTree)

hash_table = hashMap(10)

# insert some values
hash_table.set_val('gfg@example.com', 'some value')
print(hash_table)
print()

hash_table.set_val('portal@example.com', 'some other value')
print(hash_table)

print(hash_table.get_val('portalexample.com'))
print()

# delete or remove a value
hash_table.del_val('portal@exaple.com')
print(hash_table)