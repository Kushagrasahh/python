import array as arr
a=arr.array( 'i', [1,2,3,4,5,6,7])
d=arr.array( 'd',[])
for i in range (len(a)):
    k=(i/3)
    d.append(k)
print(d)