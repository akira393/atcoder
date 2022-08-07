import numpy as np
N,L,R = map(int, input().split())
A = list(map(int, input().split()))

if A.max()>L:
    A[A.argmax()]=L




# 一番小さい数字を