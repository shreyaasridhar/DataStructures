t=input()
for x in range(t):
    i=input()
    b=[]
    b=map(int,raw_input().split())
    sum=0   
    for i in range(0,len(b)):
        if b[i]>0:
            #print i,sum,b[i]
            sum+=b[i]
    for i in range(1,len(b)):
        b[i]+=b[i-1]
    m=max(b)    
    print str(m)+" "+str(sum)
