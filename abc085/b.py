# 入力関連
# import io
# import sys
# _INPUT = """\
# 4 10
# """
# sys.stdin = io.StringIO(_INPUT)

N= int(input())


d=[]
ans=0
for n in range(N):
    d.append(int(input()))

d=sorted(set(d))
print(len(d))

# 文字列関連
# 文字列判定（大文字の数が2つかどうかの判定）
# if sum(map(str.isupper,s))!=2:
    