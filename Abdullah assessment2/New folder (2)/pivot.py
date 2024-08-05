
def findpivot(nums):
    pivot=-1
    for i in range(0, len(nums), 1):
        left = 0
        right = 0
        for j in range(0, i, 1):
            left = left + nums[j]
        for k in range(len(nums)-1, i, -1):
            right = right + nums[k]
        if (right == left):
            return i
    return pivot
s=str(input())
k=list(s.split(","))
l=[]
for i in k:
    l.append(int(i))

print(findpivot(l))