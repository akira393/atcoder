N= int(input())
Pi = list(map(int, input().split()))


cnt = 0

parenent=0

for n in reversed(range(2,N+1)):

    if parenent==0:
        parenent=Pi[n-2] #人nの親
        cnt+=1
    elif parenent==n:
        parenent=Pi[n-2] #人nの親
        cnt+=1
print(cnt)

