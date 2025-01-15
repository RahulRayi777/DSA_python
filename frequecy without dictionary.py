a=[1, 2, 2, 3, 3, 3,3]
l=[]
for i in a:
    if i not in l:
        count=0
        for j in a:
            if i==j:
                count=count+1
        l.append(i)
        print(l)
        print(f"Number {i} occurs {count} times.")

        
