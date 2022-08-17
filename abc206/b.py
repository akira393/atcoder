# import io
# import sys
# _INPUT = """\
# 4 10
# """
# sys.stdin = io.StringIO(_INPUT)

N= int(input())

i=1
ans=0
while True:
    ans+=i
    if ans>=N:
        break
    i+=1

print(i)