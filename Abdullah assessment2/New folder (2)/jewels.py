jewels =str(input())
stones =str(input())
res=0
for i in jewels:
    res=res+stones.count(i)
print(res)
#print("it is okay")
