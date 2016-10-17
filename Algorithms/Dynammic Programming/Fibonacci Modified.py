i,j,k=raw_input().split()
i=int(i)
j=int(j)
k=int(k)
for x in range(k-2):
    temp=j
    j=i+(j*j)
    i=temp
print j    
