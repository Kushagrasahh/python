def nearestPower(A, B):
    ##Your code here
    ##return the closest power
    
    for i in range(100000000):
        if A**i==B:
            return A**i
            
        if A**i>B:
            g=A**(i-1)
            j=A**(i)
            K=abs(g-B)
            P=abs(j-B)
            Q=min(K,P)
            if Q==K:
                return g
            return j  

print(nearestPower(2,7))