# 入力関連
# import io
# import sys
# _INPUT = """\
# 4 10
# """
# sys.stdin = io.StringIO(_INPUT)


# 500 円玉を A 枚、100 円玉を B 枚、50 円玉を C 枚
A= int(input())
B= int(input())
C= int(input())
X= int(input())

sum_num=0
count=0
for a in range(0,A+1):
    for b in range(0,B+1):
        for c in range(0,C+1):
            sum_num=500*a+100*b+50*c
            if sum_num==X:
                count+=1
print(count)