# import io
# import sys
# _INPUT = """\
# 4 10
# """
# sys.stdin = io.StringIO(_INPUT)

# N= int(input())

# M = map(int, input().split())
M = list(map(int, input().split()))

N,M=map(int, input().split())

edge=[[False]*N for _ in range(N)]

A=[]
ans=0
for n in range(N):
    _A = list(map(int, input().split()))
    A.append(_A)