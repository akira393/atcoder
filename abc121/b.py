# import io
# import sys
# _INPUT = """\
# 2 3 -10
# 1 2 3
# 3 2 1
# 1 2 2
# """
# sys.stdin = io.StringIO(_INPUT)

N,M,C=map(int, input().split())
B = list(map(int, input().split()))

A=[]
ans=0
for n in range(N):

    _A = list(map(int, input().split()))
    count=0
    for m in range(M):
        count=count+_A[m]*B[m]
    if count+C>0:
        ans+=1
print(ans)