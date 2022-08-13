# import io
# import sys
# _INPUT = """\
# 4 10
# """
# sys.stdin = io.StringIO(_INPUT)

N= int(input())


ans_excluded=int((N+0.9999999999)/1.08)
ans_included=int(int(ans_excluded)*1.08)

if N!=ans_included:
    print(":(")
else:
    print(int(ans_excluded))
