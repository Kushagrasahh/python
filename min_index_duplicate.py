def minimumindexduplicate(arr):
    #note-- arr elements will be less than arr size
    mini=len(arr)
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                mini=min(mini,j)
                
    if mini==len(arr):
        return -1
    else:
        return arr[mini] 

arr=[2,1,3,5,3,2]
print(minimumindexduplicate(arr))                    

