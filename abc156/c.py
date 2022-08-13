# import io
# import sys
# _INPUT = """\
# 4 10
# """
# sys.stdin = io.StringIO(_INPUT)
from decimal import Decimal, ROUND_HALF_UP

N= int(input())
# N, M = map(int, input().split())
# M = map(int, input().split())
X = list(map(int, input().split()))


_p=sum(X)/N
_p_str=str(_p)
p=Decimal( _p_str ).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
ans=0

for i in range(N):
    ans+=(X[i]-p)**2


print(ans)