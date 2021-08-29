def two(a1,a2,v):
    for i in range(len(a1)):
        k=v-a1[i]
        if k in a2:
           return True
    return False   
    
                   
a1=[0,0,-5,30212]
a2=[-10,40,-3,9]
v=-8
print(two(a1,a2,v))            