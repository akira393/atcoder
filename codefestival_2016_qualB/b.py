# import io
# import sys
# _INPUT = """\
# 12 5 2
# cabbabaacaba
# """
# sys.stdin = io.StringIO(_INPUT)


N,A,B=map(int, input().split())

S= list(str(input()))

cnt_b=1
cnt=0
for s in S:
    if s=="c":
        print("No")
    elif s=="a":
        if cnt<A+B:
            print("Yes")
            cnt+=1
        else:
            print("No")
    elif s=="b":
        if cnt<A+B and cnt_b<=B:
            print("Yes")
            cnt+=1
        else:
            print("No")
        cnt_b+=1