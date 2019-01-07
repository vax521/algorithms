# 当连续N天每天收到N枚金币后，骑士会在之后的连续N+1天里，每天收到N+1枚金币。
# 请计算在前K天里，骑士一共获得了多少金币。
day = int(input("请输入第几天："))
result_sum = 0
a = []
# N = 1
# for i in range(1,int(day)):
#     for j in (1,N):
#         if  i <= int(day):
#             a.append(N)
#     N += 1
# print(a)
count = 0
print(day)
for i in range(1,day):
    for j in range(i):
        a.append(i)
        count += 1
        if count == day:
            break
    if count == day:
        break
print(a)
print(sum(a[:day]))