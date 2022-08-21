# # 入力関連
# import io
# import sys
# _INPUT = """\
# 10 25 10
# """
# sys.stdin = io.StringIO(_INPUT)

X,Y,N=map(int, input().split())
ans=0
# 一個の個数
for a in range(0,100+1):
    # 三個の個数
    for b in range(0,100+1):
        if a*1+b*3==N:
            if ans!=0:
                ans=min(ans,a*X+b*Y)
            else:
                ans=a*X+b*Y
print(ans)