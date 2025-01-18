words = ["eat", "tea", "tan", "ate", "nat", "bat"]
l = []

for i in words:
    group = []
    for j in words:
        if sorted(i) == sorted(j) and j not in group:
            group.append(j)
    if group not in l:
        l.append(group)

print(l)
