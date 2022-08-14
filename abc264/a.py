# import io
# import sys
# _INPUT = """\
# 4 10
# """
# sys.stdin = io.StringIO(_INPUT)

# N= int(input())
# N, M = map(int, input().split())
# M = map(int, input().split())

L,R=map(int, input().split())


atcoder_list=list("atcoder")

a="".join(atcoder_list[L-1:R])
print(a)
