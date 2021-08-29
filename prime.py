def prime(n):
    x=[2,3,5,7]
    for num in range(3,n+1,2):
        if all(num%i!=0 for i in x):
            x.append(num) 
    return x
print(prime(500))            