import itertools
N, M = map(int, input().split())
result=list(itertools.combinations(range(1,M+1), N))
for re in result:
    
    print(" ".join(map(str,list(re))))