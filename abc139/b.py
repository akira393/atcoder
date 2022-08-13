# import io
# import sys
# _INPUT = """\
# 4 10
# """
# sys.stdin = io.StringIO(_INPUT)

A,B=map(int, input().split())

ans=1

# 一つで良い時は、タップは0よね
if 1!=B:
    notuse_sashikomiguchi=A
    # A-1個づつ増やしていける
    while B>notuse_sashikomiguchi:
        notuse_sashikomiguchi=notuse_sashikomiguchi-1+A
        ans+=1
else:
    ans=0
print(ans)