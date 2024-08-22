def reverse(s):
    return s[::-1]
def binarytoint(n):

    s=0
    p=0
    for i in n:
        if(i=='1'):
            s=s+((2**p))
        p+=1
    return s


s=str(input("Enter number:"))

l=list(s.split(","))
for i in l:
    k=reverse(i)
    if(binarytoint(k)%5==0):
       print(i)
 print("forked by laxmi")       
        
        
