l=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

def minenergy(l):
    i0=0
    i1=0
    for i in range(0,len(l),1):
        i0=i0+l[i]
        i=i+1
    for i in range(1,len(l)-1,1):
        i1=i1+l[i]
        i=i+1
    return min(i0,i1)
print(minenergy(l))