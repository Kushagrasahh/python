n=int(input("enter no"))
list=[]
for j in range(2,n):
    for i in range (1,11):
        g=j*i
        list.append(g)

print(list)