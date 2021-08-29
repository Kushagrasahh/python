def makeProductOne( arr, N):
        # code here 
        neg=zero=ans=0
        for i in arr:
            if i>0:
                ans+=i-1
            elif i==0:
                zero+=1
            elif 0>i:
                neg+=1
                ans+=abs(i)-1
            
        if neg%2==0:
            return ans+zero
        else:
            if zero!=0:
                return ans+zero
            else:
                return ans+2