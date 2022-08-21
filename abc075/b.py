
# import io
# import sys
# _INPUT = """\
# 3 5
# .....
# .#.#.
# .....
# """
# sys.stdin = io.StringIO(_INPUT)
# 左上、上、右上、左、右、左下、下、右下
DX=[-1,-1,-1,0,0,1,1,1]
DY=[-1,0,1,-1,1,-1,0,1]

H,W=map(int, input().split())
S=[]
for n in range(H):
    S.append(list(input()))
edge=[[0]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j]=="#":
            edge[i][j]=S[i][j]
            continue
        for dx,dy in zip(DX,DY):
            ni=i+dx
            nj=j+dy
            if ni<0 or ni>=H or nj<0 or nj>=W:
                continue
            if S[ni][nj]=="#":
                edge[i][j]+=1
for e in edge:
    print(*e,sep='')