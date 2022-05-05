hash_table = {}

# insert some values
hash_table['1'] = 'some value 1'
print(hash_table)

hash_table['2'] = 'some other value 2'
print(hash_table)
hash_table['3'] = 'some other value 3'
print(hash_table)

# search/access a record with key
print("peeking some value :" + hash_table['1'])
print(hash_table)
# get some value out if not present will return not found
print("getting a value pop out :" + hash_table.pop('1', 'not found'))

# delete or remove a value
print("deleting some value")
del hash_table['2']


print(hash_table)