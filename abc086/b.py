# import io
# import sys
# _INPUT = """\
# 12 1
# """
# sys.stdin = io.StringIO(_INPUT)

a,b=map(str, input().split())
num=int(a+b)
x=int(num**0.5)
if x**2==num:
    print("Yes")
else:
    print("No")