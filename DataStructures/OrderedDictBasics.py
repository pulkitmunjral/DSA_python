# same as dictionary and preserve the order of input
from collections import OrderedDict

oDic = OrderedDict()
for i in range(10):
    oDic[i] = i

print(oDic)

# pass key to move it to last
oDic.move_to_end(1)
print(oDic)

# to remove the first item
print(oDic.popitem(last=False))


# to remove last item of the list
print(oDic.popitem(last=True))
