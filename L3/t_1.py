ids = {'user1': [213, 213, 213, 15, 213],
'user2': [54, 54, 119, 119, 119],
'user3': [213, 98, 98, 35]}

z = []
for x in ids.values():
    z += x

print(set(z))
