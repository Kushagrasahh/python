def prime(n):
    p=[]
    k=[]
    for i in range(1,n+1):
       if i%2==0:
           p.append(i) 
       else:
           k.append(i)
           
    
    print(k)   
prime(25)       
