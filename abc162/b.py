# import io
# import sys
# _INPUT = """\
# 4 10
# """
# sys.stdin = io.StringIO(_INPUT)

N= int(input())
ans=0
for i in range(1,N+1):
    if i%3==0 or i%5==0:
        continue
    ans+=i

print(ans)
