def remove(s, k):

    if k > len(s):
        return s
    else:
        # USING REPLACE
        s = s.replace(s[k], '')
        # USING STRING SLICING
        s=s[0:k]+s[k+1:len(s)]
        return s


d = remove("PYTHON", 5)
print(str(d))


