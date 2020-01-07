try:
    def minHits(s,w):
        if(len(w)==0):
            return 0
        c=0
        temp=s
        for i in range(0,len(w)):
            s-=w[i]
            if(s==0):
                c=i
                break;
            if(s<0):
                c=i-1
                break;
            if(i==len(w)-1 and s!=0):
                return 1
                
        ans= minHits(temp,w[c+1:])+1
        return ans

    t = int(input())
    i=0
    while(i<t):
        n = [int(x) for x in input().split()]
        print(minHits(n[0],n[1:]))
        i+=1
except Exception:
   pass