def arr(n):
    from collections import Counter
    d=Counter(n)
    x=[]
    for i in d:
        if d[i]==2:
            x.append(i)
    return len(x)
print(arr(['tom','jerry','doramon','jerry','rat','tom','rat','rat']))            
