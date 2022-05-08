
fr1 = frozenset([1, 2, 3, 3, 4, 5, 4])
fr2 = frozenset([4, 5, 4, 5, 6])

print(fr1, fr2)

print("union of 2 sets with help of or operator |")
print(fr1 | fr2)

print("intersection of 2 sets with help of and operator &")
print(fr1 & fr2)

print("check if 1 is subset of 2 with help of lessthan operator <")
print(fr1 < fr2)

print("difference of 2 sets with help of minus operator -")
print(fr1 - fr2)
print(fr2 - fr1)