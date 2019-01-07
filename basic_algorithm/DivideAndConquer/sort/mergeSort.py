
def mergeSort(seq):
    # 分解
    mid = len(seq)//2
    left_seq,right_seq = seq[:mid],seq[mid:]
    print(left_seq)
    print(right_seq)
    # 分治
    if len(left_seq) > 1: left_seq = mergeSort(left_seq)
    if len(right_seq) > 1: right_seq = mergeSort(right_seq)
    # 合并
    res = []
    while left_seq and right_seq:
        # 两者尾部较大者弹出
        if left_seq[-1] >= right_seq[-1]:
            res.append(left_seq.pop())
        else:
            res.append(right_seq.pop())
    res.reverse()
    return (left_seq or right_seq)+res

if __name__ == '__main__':
    array1 = [1,23,54,56,66,45]
    print(mergeSort(array1))