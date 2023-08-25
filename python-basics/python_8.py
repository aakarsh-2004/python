# sets
#sets do not have duplicate elements, if you enter it anyways it's gonnna remove it
a = {1, 2, 3, 5, 6}
b = {5, 6}

a.add(4)
# a.clear()
print(a.difference(b))
print(a.intersection(b))
print(a.union(b))

a.discard(1)
# updating a set so that only the difference is left
# a.difference_update(b)

print(a.isdisjoint(b))
print(b.issubset(a))
print(a.issuperset(b))

print(5 in a and 5 in b)
print(list(a))