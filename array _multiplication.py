def isPrime(n):
    count=0
    if n==1:
        return 0
    else:
        pass    
    for i in range(1,n+1):

        if n%i==0:
            count+=1

    if count<=2:
        return 1
    else:
        return 0    

print(isPrime(1))