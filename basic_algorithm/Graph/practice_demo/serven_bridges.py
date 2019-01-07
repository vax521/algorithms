
graph = [[0, 1, 2, 2], [1, 0, 1, 1], [2, 1, 0, 0], [2, 1, 0, 0]]


def count_num(mat):
    # 度为奇数的节点个数
    count = 0
    for i in range(0, len(mat)):
        degree = 0
        for j in range(0, len(mat[i])):
            degree += mat[i][j]
        if degree % 2 == 1:
            count += 1
        print(degree)
    return count


num = count_num(graph)
if num > 2:
    print("有{}个地方通奇数的桥，不存在欧拉回路！\n".format(num))
elif num == 2 or num==0:
    print("存在欧拉回路！")

