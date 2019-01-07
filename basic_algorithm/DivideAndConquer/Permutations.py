# 求一个算法：N个数，用其中M个任意组合相加等于一个已知数X。得出这M个数是哪些数。
# 比如：
# seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# s = 14 # 和
# 全部可能的数字组合有：
# 5+9, 6+8
# 1+4+9, 1+5+8, 1+6+7, 2+3+9, 2+4+8, 2+5+7, 3+4+7, 3+5+6
# 1+2+5+6, 1+3+4+6, 1+2+4+7, 1+2+3+8, 2+3+4+5
# 共计15种

# 方法一 暴力法
# 版本一（纯计数）
def find(seq, s):
    n = len(seq)
    if n==1:
        return [0, 1][seq[0]==s]
    
    if seq[0]==s:
        return 1 + find(seq[1:], s)
    else:
        return find(seq[1:], s-seq[0]) + find(seq[1:], s)

def find2(seq, s, temp=""):
    if len(seq) == 0:
        return 
    if seq[0] == s:
       print(temp+str(seq[0])) # 找到一种则打印
    find2(seq[1:],s,temp)      # 不包含seq[0]
    find2(seq[1:],s-seq[0],str(str(seq[0])+"+"+temp))# 包含seq[0]


if __name__ == '__main__':
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sum =  14
    print(find(seq, 14))
    print(find2(seq,14))
