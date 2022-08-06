Y=int(input())
extra=Y%4

if extra==2:
    print(Y)
elif extra==0:
    print(Y+2)
elif extra==1:
    print(Y+1)
elif extra==3:
    print(Y+3)