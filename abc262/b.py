N,M=map(int, input().split())

edge=[[False]*N for _ in range(N)]

for m in range(1,M+1):
    u,v=map(int,input().split())
    u-=1
    v-=1
    edge[u][v]=True
    edge[v][u]=True

cnt=0
for a in range(N-2):
    for b in range(a+1,N-1):
        for c in range(b+1,N):
            if edge[a][b] and edge[b][c] and edge[c][a]:
                cnt+=1

print(cnt)