def insertion_sort(arr):
    n=len(arr)
    for current in range(1,n):
        currentcard=arr[current] 
        correct_position=current-1 
        while correct_position>=0:
            if (currentcard>arr[correct_position]):
                break
            else:
                arr[correct_position+1]=arr[correct_position]
                correct_position=correct_position-1
            arr[correct_position+1]=currentcard
    return arr
arr = [12,25,11,34,90,22]
sorted_list = insertion_sort(arr)
print("Sorted Elements :", sorted_list)

'''
Debugging Steps
1)For iterating I took length of list(n)
2)
currentcard=arr[1]#25
correctposition=1-0#0
while condition
if arr[0]#12<25:
this is true
then it break
goes for second iteration
currentcard=arr[2]#11
correctposition#2-1#1
while condition
if arr[2]#25<11
false
goes to else
arr[1+1]=arr[1]
arr[2]=arr[1]
arr[2]=25
correctposition=correctposition-1#1-1 =0
next it will check for 1 if it is less than that
then we need to set the current card at correctposition+1
finnaly return the array
'''
