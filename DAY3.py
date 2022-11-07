i=[]
for n in range(10,150):
    if(n%15==0) and (n%5==0):
        i.append(str(n))
print(','.join(i))
