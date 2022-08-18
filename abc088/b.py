# import io
# import sys
# _INPUT = """\
# 4
# 20 18 2 18
# """
# sys.stdin = io.StringIO(_INPUT)

N= int(input())

A = list(map(int, input().split()))

A=sorted(A,reverse=True)
Alice=[A[i] for i in range(len(A)) if i%2==0]
Bob=[A[i] for i in range(len(A)) if i%2==1]

print(sum(Alice)-sum(Bob))