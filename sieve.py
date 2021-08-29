n=int(input("Enter no where you want to find your prime no: \n"))
k=[]
for i in range(n+1):
    k.append(i)
k[0]=0
k[1]=0

p=2
while(p * p <= n):
   
    if (p!=0):
       for i in range(p*2, n+1, p):
           k[i]=0

    p+=1
#using loop to print prime no
for i in range(len(k)):
    if (k[i] != 0):
        print(k[i],end=" ") #prints list containg only primes

print("\n") 
print(k,end="") #prints original list     