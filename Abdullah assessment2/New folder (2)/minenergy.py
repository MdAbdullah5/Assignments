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


def min_cost_climbing_stairs(energy):
    n = len(energy)
    dp = [0] * n
    dp[0] = energy[0]
    dp[1] = energy[1]

    for i in range(2, n):
        dp[i] = min(dp[i - 1], dp[i - 2]) + energy[i]

    return min(dp[-1], dp[-2])
print(min_cost_climbing_stairs(l))