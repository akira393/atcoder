# 入力関連
# import io
# import sys
# _INPUT = """\
# 4 10
# """
# sys.stdin = io.StringIO(_INPUT)

X= int(input())

ans=1
for x in range(2,X+1):
    for p in range(2,100):
        if ans<=x**p and x**p<=X:
            ans=x**p
        

print(ans)
