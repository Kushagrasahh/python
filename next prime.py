def next_prime(n):
    x=[2,3,5,7]
    for num in range(n,n+5):
        if all(num%i!=0 for i in x):
            return num
        
print(next_prime(49))




