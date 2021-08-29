def avg(s):
    d = sum(s)/len(s)
    return d


s = [78,8,9,54,63,5]
    
if sum(s) != 0:
      print(avg(s))

try:
    print("the average is " + avg(s))
except Exception as e:
    print("the average is 0.0")    



            



