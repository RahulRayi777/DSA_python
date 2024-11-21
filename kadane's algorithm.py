l=[1,-10,2,3]
global_sum=l[0]
curr_sum=0
for num in l:
    curr_sum=curr_sum+num
    if curr_sum<0:
        curr_sum=0
    else:
        curr_sum=max(global_sum,curr_sum)
print(curr_sum)
