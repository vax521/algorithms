# 求一个字符串的所有排列
count = 0 
def pailie(input_string,temp):
    global count
    # 结束条件
    if len(input_string)==0:
        count += 1
        print(temp)
        return 
    for i  in range(len(input_string)):
        # 选择
        new_string = input_string[0:i]+input_string[i+1:]
        pailie(new_string,temp+input_string[i])
   

if __name__ == '__main__':
    pailie("afasdgf","")
    print("排列数："+str(count))
