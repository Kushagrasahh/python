def alternating(n):

    for i in range(len(n)):
        for j in range(1, len(n), 2):
            for k in range(2, len(n), 2):
                if n[k] % 2 == 0:
                    return True
                else:
                    return False
            if n[j] % 2 != 0:
                return True
            else:
                return False

        if n[0] % 2 == 0:
            return True
        else:
            return False
    if n == []:
        return True


p = alternating([10, 9, 9, 6])
print(p)
k = alternating([10, 15, 8])
print(k)
l = alternating([10])
print(l)
m = alternating([])
print(m)
b = alternating([10, 15, 9])
print(b)
l1 = alternating([6, 7, 8, 5, 6, 7, 8])
print(l1)
