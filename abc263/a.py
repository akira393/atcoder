# N= int(input())
# N, M = map(int, input().split())
# M = map(int, input().split())
M = list(map(int, input().split()))

cmt=0
if len(list(set(M)))==2:
    a,b=list(set(M))
    for m in M:
        if a==m:
            cmt+=1
    if cmt==2 or cmt ==3:
        print("Yes")
    else:
        print("No")

else:
    print("No")