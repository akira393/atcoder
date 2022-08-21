# 入力関連
# import io
# import sys
# _INPUT = """\
# 4 10
# """
# sys.stdin = io.StringIO(_INPUT)

N,Y=map(int, input().split())
# マン円
a=-1
# ５０００
b=-1
# 千円
c=-1

for an in range(N+1):
    for bn in range(N+1):
        if an+bn>N:
            break
        cn=N-an-bn
        if an*10000+bn*5000+1000*cn==Y:
            a,b,c=an,bn,cn
            break
    if a!= -1 and b!=-1 and c!=-1:
        break
print(a,b,c)
            

# 文字列関連
# 文字列判定（大文字の数が2つかどうかの判定）
# if sum(map(str.isupper,s))!=2:
    