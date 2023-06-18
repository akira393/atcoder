# 入力関連
# import io
# import sys
# _INPUT = """\
# 4 10
# """
# sys.stdin = io.StringIO(_INPUT)

from collections import defaultdict

N= int(input())

ans=0
# bucket=[0]*(100+1)
s=defaultdict(int)
for n in range(N):
    _s=list(input())
    s["".join(sorted(_s))]+=1
print(int(sum([s[x]*(s[x]-1)/2 for x in s])))
# ans=max([s[x] for x in s])-1

# 別解
