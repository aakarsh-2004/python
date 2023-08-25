arr = ['a', 'b', 'c', 'c', 'd', 'a']

new_arr = set([item for item in arr if arr.count(item) > 1])
print(new_arr)