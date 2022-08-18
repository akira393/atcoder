# import io
# import sys
# _INPUT = """\
# AtCoCo
# """
# sys.stdin = io.StringIO(_INPUT)

from curses.ascii import islower, isupper


S= input()

def isAC(s:list)->bool:
    """ACかどうか判定する関数

    Args:
        s (list): 入力となるリスト文字列

    Returns:
        bool: 判定結果
    """
    # 先頭がA
    if s[0]!="A":
        return False
    # Cの数が1個
    if s[2:-1].count("C")!=1:
        return False
    # 大文字は2つまで
    if sum(map(str.isupper,s))!=2:
        return False

    return True    

print("AC" if isAC(S) else "WA")