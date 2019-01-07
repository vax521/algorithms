# 分治法 最近点对问题

import math
import random

def get_distance(pairs):
    return math.sqrt((pairs[0][0]-pairs[1][0])**2+(pairs[0][1]-pairs[1][1])**2)

def candidateDot(u,right,dis,mid_x):
     #遍历right（已按横坐标升序排序）。
     # 若横坐标小于med_x-dis则进入下一次循环；
     # 若横坐标大于med_x+dis则跳出循环.
     # 若点的纵坐标好是否落在在[u[1]-dis,u[1]+dis]，则返回这个点
    for v in right:
        if v[0] < mid_x-dis:
            continue
        if v[0] > mid_x+dis:
            break
        if v[1]>=u[1]-dis and v[1]<=u[1]+dis:
            yield v

# 求出横域两个部分的点的最小距离
def combine(left,right,resMin,med_x):
    dis = resMin[1]
    minDis = resMin[1]
    pair = resMin[0]
    for left_point in left:
        if left_point[0] < med_x-dis:
            continue
        for right_point in candidateDot(left_point,right,dis,med_x):
            dis  = get_distance([left_point,right_point])
            if dis < minDis:
                minDis = dis
                pair=[left_point,right_point]
    return [pair,minDis]



# 分治求解
def divide(seq):
    n = len(seq)
    seq = sorted(seq)
    if n<=1:
        return None,float('inf')
    elif n == 2:
        return [seq,get_distance(seq)]
    else:
        half = int(len(seq)/2)
        med_x = (seq[half][0]+seq[-half-1][0])/2
        left = seq[:half]
        resLeft = divide(left)
        right = seq[half:]
        resRight = divide(right)
        if resLeft[1]<resRight[1]:
            resMin = combine(left,right,resLeft,med_x)
        else:
            resMin = combine(left,right,resRight,med_x)
        pair = resMin[0]
        minDis = resMin[1]
    return [pair,minDis]

if __name__ == '__main__':
    points = [(random.randint(0,1000),random.randint(0,1000)) for i in range(100)]
    print(divide(points))