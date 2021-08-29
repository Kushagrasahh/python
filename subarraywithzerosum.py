def subarray(arr):
    m=0
    b=set()
    for i in range(len(arr)):
         m+=arr[i]
         if(arr[i]==0 or m in b or m==0):
             return True
         else:
             b.add(m)
    return False

print(subarray([4,2,-3,1,6]))                 

