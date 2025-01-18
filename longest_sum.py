nums = [1, -2, 3, 4, -1, 2, 1, -5, 4]
curr_sum=max_sum=nums[0]
for num in nums[1:]:
    curr_sum=max(num,curr_sum+num)
    max_sum=max(max_sum,curr_sum)

print(max_sum)
