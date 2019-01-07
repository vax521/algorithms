# 通过动态规划解决0-1背包问题
import numpy as np 

def solve(value_list,weight_list,totalWeight,totalNum):
    resArr = np.zeros((totalWeight)+1,dtype=np.int32)
    for i in range(1,totalNum+1):
    #     for j in range(1,totalWeight+1):
    #         if weight_list[i] <= j:
    #             resArr[i,j] = max(resArr[i-1,j-weight_list[i]]+value_list[i],resArr[i-1,j])
    #             print(resArr[i,j])
    #         else:
    #             resArr[i,j] = resArr[i-1,j]
    # return resArr[-1,-1]
        # 改进版
        for j in range(totalWeight,0,-1):
            if weight_list[i] <= j:
                resArr[j] = max(resArr[j],resArr[j-weight_list[i]]+value_list[i])
                print(resArr[j])
    return resArr[-1]
    
if __name__=="__main__":
    v = [0,60,100,120]
    w = [0,10,20,30]
    weight = 50
    n = 3
    result = solve(v,w,weight,n)
    print(result)
