H,W=map(int, input().split())



ans=int(H*W/2)
if H==1 or W==1:
    print(1)
elif H*W%2:
    print(ans+1)
else:
    print(ans)
