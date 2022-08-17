import io
import sys
_INPUT = """\
14 2 4
"""
sys.stdin = io.StringIO(_INPUT)



N,A,B=map(int, input().split())

N_list=[]
ans=0
for n in range(1,N+1):
    _n=list(str(n))
    _n=[int(x) for x in _n]
    if A<=sum(_n) and sum(_n)<=B:
        ans+=n
    
print(ans)