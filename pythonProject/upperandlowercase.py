s=str(input("Enter Sentence:"))
c=0
l=0
for a in s:
    if(a>='a' and a<='z'):
        c+=1
    elif(a>='A' and a<='Z'):
        l+=1
print("Capital=",l,"Lower=",c)