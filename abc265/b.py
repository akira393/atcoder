# 入力関連
# import io
# import sys
# _INPUT = """\
# 4 10
# """
# sys.stdin = io.StringIO(_INPUT)

# Tはライフ
# Nは移動回数
# Mは回復できる数
N,M,T=map(int, input().split())
A = list(map(int, input().split()))

X=[]
Y=[]
bounase=[0]*(N+1)
ans=0
for m in range(M):
    _X,_Y=map(int, input().split())
    bounase[_X]=_Y

ans="Yes"

for n in range(N-1):
    T+=bounase[n+1]
    T-=A[n]
    if T<=0:
        ans="No"
        break
print(ans)
    

