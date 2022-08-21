# 入力関連
# import io
# import sys
# _INPUT = """\
# 4 10
# """
# sys.stdin = io.StringIO(_INPUT)

# N= int(input())
# M = map(int, input().split())
H,W=map(int, input().split())


XY={"U":{"X":-1,"Y":0},"D":{"X":1,"Y":0},"R":{"X":0,"Y":1},"L":{"X":0,"Y":-1}}

G=[]
ans=0
for n in range(H):
    _G = list(input())
    G.append(_G)
i,j=0,0
cnt=10**6
while H-1>=i>=0 and W-1>=j>=0:
    _i=i+XY[G[i][j]]["X"]
    _j=j+XY[G[i][j]]["Y"]
    if not (H-1>=_i>=0 and W-1>=_j>=0):
        break
    i=_i
    j=_j
    cnt-=1
    if cnt<=0:
        break
if cnt<=0:
    print(-1)
else:
    print(i+1,j+1)

