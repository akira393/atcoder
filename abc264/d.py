import numpy as np

def idx_of_the_nearest(data, value):
    # 0は取り除きたい（確定した要素だからね）
    _data=[x for x in data if x != 0]
    idx = np.argmin(np.abs(np.array(_data) - value))
    
    return _data[idx]

import io
import sys
_INPUT = """\
catredo
"""
sys.stdin = io.StringIO(_INPUT)



S= str(input())

S_list=list(S)
atcoder_list=list("atcoder")

# for i in atcoder_list:
count=0
while S_list!=atcoder_list:
    print(S_list)
    min_value=0
    sabun_list=[]
    for index,s in enumerate(S_list):
        atcoder_list_index=atcoder_list.index(s)
        # print(index,s,atcoder_list_index)
        # なるべく変化量が小さいもの 
        sabun_list.append(index-atcoder_list_index)
    min_value=idx_of_the_nearest(sabun_list, 0)
    for index,s in enumerate(S_list):
        atcoder_list_index=atcoder_list.index(s)
        if index-atcoder_list_index==min_value:
            if atcoder_list_index-index<0:
                # 自身と一個前を入れ替える
                S_list[index]=S_list[index-1]
                S_list[index-1]=s
                count+=1
                break
            elif atcoder_list_index-index>0:
            
                # 自身と一個後ろを入れ替える
                S_list[index]=S_list[index+1]
                S_list[index+1]=s
                count+=1
                break


print(count)