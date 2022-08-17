# import io
# import sys
# _INPUT = """\
# 4 10
# """
# sys.stdin = io.StringIO(_INPUT)

N= int(input())

A = list(map(int, input().split()))


count=0
can_do=True
while True:
    for an in A:
        if an%2!=0:
            can_do=False
            break
    if not can_do:
        break
    for i in range(N):
        A[i]/=2

    count+=1

print(count)