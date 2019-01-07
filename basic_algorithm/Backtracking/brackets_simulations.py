"""
给出n对括号，求括号排列的所有可能性。
"""
"""
回溯法三要素：
1、选择。在这个例子中，解就是一个合法的括号组合形式，而选择无非是放入左括号，还是放入右括号；
2、条件。在这个例子中，选择是放入左括号，还是放入右括号，是有条件约束的，不是随便放的。
而这个约束就是括号的数量。只有剩下的右括号比左括号多，才能放右括号。只有左括号数量大于0才能放入左括号。这里if的顺序会影响输出的顺序，但是不影响最终解；
3、结束。这里的结束条件很显然就是，左右括号都放完了。
"""
def BackTracking(sublist,results,left_brackets,right_brackets):
    if left_brackets==0 and right_brackets == 0:
        results.append(sublist)
    if left_brackets > 0:
        BackTracking(sublist+'(',results,left_brackets-1,right_brackets)
    if  right_brackets>left_brackets:
        BackTracking(sublist+")",results,left_brackets,right_brackets-1) 

if __name__ == '__main__':
    num = 1
    left_brackets = right_brackets = num # 左括号、右括号各有num个
    results = []
    BackTracking("",results,left_brackets,right_brackets)
    for result in results:
        print(result)

    