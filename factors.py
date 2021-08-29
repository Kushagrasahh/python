l=[]
def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
        else:
            pass
factors(13)
print(l)        

