def kl(a, b, n):
    jK = [a[i] for i in range(n-1)]
    if jK == b:
        return n-1
        
    else:
        for i in range(n-1):
            if a[i] != b[i]:
                return i
                


a = [1, 2, 3, 4]
b = [1, 2, 3]
n = 4
print(kl(a, b, n))
