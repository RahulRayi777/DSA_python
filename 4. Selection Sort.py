def selection_sort(arr):
    n=len(lst)

    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
                arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
            

#for each iteration we select the min index we keep that at right or ith position 
#like this we select the min index thats the us of the selection sort 
                
lst = [64, 25, 27, 22, 11]
print(selection_sort(lst))
