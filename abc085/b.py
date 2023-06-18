# 入力関連
# import io
# import sys
# _INPUT = """\
# 4 10
# """
# sys.stdin = io.StringIO(_INPUT)

# N= int(input())
# d=[]
# ans=0
# for n in range(N):
#     d.append(int(input()))

# d=sorted(set(d))
# print(len(d))

# 別解
N= int(input())
# d=[]
ans=0
bucket=[0]*(100+1)
for n in range(N):
    d=int(input())
    bucket[d]=1

print(sum(bucket))
