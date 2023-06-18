# 入力関連
# import io
# import sys
# _INPUT = """\
# 4 10
# """
# sys.stdin = io.StringIO(_INPUT)

# N= int(input())
# M = map(int, input().split())
import numpy as np
import math
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))



# 対角線同士の交点が四角形の中にあるかどうか

# 線分ABと線分CDの交点を求める関数
def calc_cross_point(pointA, pointB, pointC, pointD):
    cross_points = (0,0)
    bunbo = (pointB[0] - pointA[0]) * (pointD[1] - pointC[1]) - (pointB[1] - pointA[1]) * (pointD[0] - pointC[0])

    # 直線が平行な場合
    if (bunbo == 0):
        return False, cross_points

    vectorAC = ((pointC[0] - pointA[0]), (pointC[1] - pointA[1]))
    r = ((pointD[1] - pointC[1]) * vectorAC[0] - (pointD[0] - pointC[0]) * vectorAC[1]) / bunbo
    s = ((pointB[1] - pointA[1]) * vectorAC[0] - (pointB[0] - pointA[0]) * vectorAC[1]) / bunbo

    # 線分AB、線分AC上に存在しない場合
    if (r <= 0) or (1 <= r) or (s <= 0) or (1 <= s):
        return False, cross_points

    # rを使った計算の場合
    distance = ((pointB[0] - pointA[0]) * r, (pointB[1] - pointA[1]) * r)
    cross_points = (pointA[0] + distance[0], pointA[1] + distance[1])

    # sを使った計算の場合
    # distance = ((pointD[0] - pointC[0]) * s, (pointD[1] - pointC[1]) * s)
    # cross_points = (int(pointC[0] + distance[0]), int(pointC[1] + distance[1]))

    return True, cross_points


result=calc_cross_point(A,C,D,B)

if result[0]:
    print("Yes")
else:
    print("No")
