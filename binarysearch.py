def binary_search(arr,target):
    arr=sorted(arr)
    start=0
    end=len(arr)

    while start<=end:
        mid=(start+end)//2
        
        if arr[mid]==target:
            return mid

        elif arr[mid]>target:
            end=mid-1

        elif arr[mid]<target:
            start=mid+1
     
    return -1 

print(binary_search([20,30,40,50,80,70],70))
