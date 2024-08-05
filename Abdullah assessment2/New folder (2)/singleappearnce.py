s=list(input().split(","))
k=0
for i in s:
    k=k^int(i)

print(k)