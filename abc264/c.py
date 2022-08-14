# import io
# import sys
# _INPUT = """\
# 4 10
# """
# sys.stdin = io.StringIO(_INPUT)

# N= int(input())
# N, M = map(int, input().split())
# M = map(int, input().split())

H1,W1=map(int, input().split())

A=[]
for n in range(H1):
    _A = list(map(int, input().split()))
    A.append(_A)
H2,W2=map(int, input().split())

B=[]
for n in range(H2):
    _B = list(map(int, input().split()))
    B.append(_B)

for i in range(H1-H2):
    
print(A)
print(B)