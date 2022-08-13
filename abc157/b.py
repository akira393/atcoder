# import io
# import sys
# _INPUT = """\
# 41 7 46
# 26 89 2
# 78 92 8
# 5
# 6
# 45
# 16
# 57
# 17
# """
# sys.stdin = io.StringIO(_INPUT)



A=[]
for _ in range(3):
    _A = list(map(int, input().split()))
    A.append(_A)
N= int(input())

edge=[[False]*3 for _ in range(3)]

for _ in range(N):
    B=int(input())
    for i in range(3):
        for j in range(3):
            if A[i][j]==B:
                edge[i][j]=True
flag=False
for i in range(3):
    if edge[i][0] and edge[i][1] and edge[i][2]:
        flag=True
for i in range(3):
    if edge[0][i] and edge[1][i] and edge[2][i]:
        flag=True

if edge[0][0] and edge[1][1] and edge[2][2]:
    flag=True
if edge[0][2] and edge[1][1] and edge[2][0]:
    flag=True

if flag:
    print("Yes")
else:
    print("No")
