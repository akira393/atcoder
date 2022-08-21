# 入力関連
# import io
# import sys
# _INPUT = """\
# 4 10
# """
# sys.stdin = io.StringIO(_INPUT)

N= int(input())
S=list(input())
ans=0
for i in range(1,len(S)):
    front_S=S[:i]
    back_S=S[i:]
    totyu=0
    for fs in set(front_S):
        for bs in set(back_S):
            
            if fs == bs:
                totyu+=1
                continue
    ans=max(totyu,ans)
print(ans)