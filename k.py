def flipCoins( N, s):
        # Code here
        if N==0:
            return 'No'
        if N==1:
            if s=='1':
                return 'Yes'
            return 'No'
            
        if N==2:
            if s=='11'or s=='00':
               return 'Yes'
            return 'No'
            
        y='00'
        l='101'
        if y in s and s.count('0')%2==0 and l not in s:
            return 'Yes'
        return 'No'

print(flipCoins(2,'10'))        