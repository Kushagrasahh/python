def sttr(s,r):
    h={}
    var=max(len(s),len(r))
    u=var+1
    v=''
    for i in range(len(s)):
        if s[i] not in h:
            h[s[i]]=i
    for c in r:
        if c  in h.keys() and h[c]<u:
            v=c
            u=h[c]
    if v:
        return v
    else:
        return '$' 
    


o=sttr("python","javath")
print(o)
