def gcd(x,y):
    k=[]
    '''if x>y:
      smaller=y
    else:
        smaller=x'''

    for i in range(1,min(x,y)+1):
        if (x%i==0) and (y%i==0):
            k.append(i)
            #print(i)
            #gcd=i
         
    return max(k)

print(gcd(54,24))    

