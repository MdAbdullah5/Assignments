o=str(input("Enter Array:"))
p=list(o.split(","))
x=input("Enter charecter:")

k=[]
for l in p:
    if(l.count(x)):
        k.append(l)
print(k)