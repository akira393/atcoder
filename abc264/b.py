# import io
# import sys
# _INPUT = """\
# 4 10
# """
# sys.stdin = io.StringIO(_INPUT)

# N= int(input())
# N, M = map(int, input().split())
# M = map(int, input().split())

R,C=map(int, input().split())

edge=[[False]*15 for _ in range(15)]
for i in range(15):
    for j in range(15):
        if i==0 or i==14:
            edge[i][j]=True
        if j==0 or j==14:
            edge[i][j]=True
for i in range(2,15-2):
    for j in range(2,15-2):
        if i==0+2 or i==14-2:
            edge[i][j]=True
        if j==0+2 or j==14-2:
            edge[i][j]=True
for i in range(4,15-4):
    for j in range(4,15-4):
        if i==0+4 or i==14-4:
            edge[i][j]=True
        if j==0+4 or j==14-4:
            edge[i][j]=True
for i in range(6,15-6):
    for j in range(6,15-6):
        if i==0+6 or i==14-6:
            edge[i][j]=True
        if j==0+6 or j==14-6:
            edge[i][j]=True

flag_blak=False
if edge[C-1][R-1]==True:
    flag_blak=True

if flag_blak:
    print("black")
else:
    print("white")