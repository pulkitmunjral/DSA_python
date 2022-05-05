import heapdict

h = heapdict.heapdict()

h['g'] = 2
h['x'] = 1
h['k'] = 4
h['s'] = 3

print("will return all the items> key-value pair from the dict")
for i in h.items():
    print(i)

print("to get all keys")
for i in h.keys():
    print(i)

print("to get all values")
for i in h.values():
    print(i)

print("to peek an item")
print(h.peekitem())

print("will return the key value pair on the basis of highest priority of value")
# here 'x' has the highest priority '1'
print(h.popitem())

print("to get value of a key if present otherwise print something else")
print(h.get('e', 'not found'))