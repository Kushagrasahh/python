def makepairs(s,k):
    s=[1,2,3,4,5]
    k=[6,7,8,9,0]
    new  = [(s[0],k[0]),(s[1],k[1]),(s[2],k[2]),(s[3],k[3]),(s[4],k[4])]
    return new

p = makepairs("s","k")
print(p)