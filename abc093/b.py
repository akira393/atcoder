# import io
# import sys
# _INPUT = """\
# 3 8 2
# """
# sys.stdin = io.StringIO(_INPUT)


A,B,K=map(int, input().split())

# for i in range(A,B+1):
#     if A+K>i or B-K<i:
#         print(i)

for i in range(A,A+K):
    if i>(B-A)/2+A:
        break
    print(i)

for j in range(B-K+1,B+1):
    if j<=(B-A)/2+A:
        continue
    print(j)