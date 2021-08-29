
def searchmany(s, x, k):

    cnt = 0
    for i in range(len(s)):
        if x == s[i]:
            cnt += 1
    if cnt == k or cnt < k:
        return True
    else:
        return False


t = searchmany([10, 17, 15, 12], 15, 1)
h = searchmany([10, 12, 12, 12], 12, 2)
o = searchmany([10, 12, 15, 11], 17, 18)
print(t)
print(h)
print(o)
