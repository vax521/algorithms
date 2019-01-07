import sys
sys.setrecursionlimit(10000000)

# 线性时间选择第K小的数
def partition(seq):
    pi = seq[0]
    lo = [i for i in seq[1:] if i <= pi]
    hi = [i for i in seq[1:] if i > pi]
    return lo, pi, hi

def select(seq,k):
    lo, pi, hi = partition(seq)
    m = len(lo)
    if m == k:
        return pi
    # 比k小，说明在较大的区间里,选第k-m-1小的
    elif m < k:
        return select(hi,k-m-1)
    else:
        return select(lo,k)

if __name__ == '__main__':
    array1 = [1,43,5,5,76,5,4,6753,63,6345,63547,89956,75]
    # for i in range(len(array1)):
    #     print(select(array1,i))
    print(select(array1,9))