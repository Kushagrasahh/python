def average(s):
    if s!=[]:
     s=sum(s)/len(s)
     return s
    else: 
        try:
            s=sum(s)/len(s)
        except Exception as e:
            print("The Average Of Your List Is : 0.0")
         
t=average([8,9,8,7,6,6,556,4])
print(t)

