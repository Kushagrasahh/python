n='3547365463836'
k=[]
for i in range(len(n)):
    k.append(n[i])
    k.sort()
v=''
for i in range(len(k)):
    v+= str(k[i])
b=len(v)
j=v[b::-1]
print(j)        