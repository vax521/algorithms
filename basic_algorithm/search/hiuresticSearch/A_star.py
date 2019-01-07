
graph = [
    [0,  0,      0,  0, 0, 0,     0],
    [0,  0,      0,  1, 0, 0,     0],
    [0,  0,      0,  1, 0, 0,     0],
    [0,  "cat",  0,  1, 0, 0,     0],
    [0,  1,      0,  1, 0, "bone", 0],
    [0,  0,      0,  0, 0, 0,      0]
]

class Node:
    # 表示从cat方块到当前方框的距离
    G = 0
    # 当前方块到目标点（我们把它称为点B，代表骨头！）的移动量估算值
    H = 0
    # G = G+H 表示路径增量
    F = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y

cat_x = 1
cat_y = 3
bone_x = 4
bone_y = 5
# 一个记录下所有被考虑来寻找最短路径的方块（称为open列表）
open = []
# 保存已确定点的横纵坐标
closed = []
width= len(graph)-1
height= len(graph[0])-1


for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == "cat":
            cat_x, cat_y = i, j
        if graph[i][j] == "bone":
            bone_x, bone_y = i, j
# print((cat_x,cat_y),(bone_x,bone_y))

# 判断一个方格是否符合条件
def is_good(x,y):
    if x >= 0 and x <= width and y>=0 and y <= height:
        if graph[x][y] != 1 and (x,y) not in closed:
            return True
        else:
            return False
    else:
        return False

# 获取当前方块到"bone"方块的距离
def get_instance(x,y):
    return abs(bone_x-x)+abs(y-bone_y)
  
# 获取具有最小F值的格子
def get_node_with_MinFValue(node_list):
    temp_set = set()
    for node in node_list:
        temp_set.add(node.F)
    if len(temp_set) == 1:
        print("F值相等，选择最后一个")
        return node_list[-1]
    else:
        sorted_node_list = sorted(node_list,key = lambda node:node.F)
        print("F值不相等，选择第一个")
        print(waited_nodes(sorted_node_list))
        return sorted_node_list[0]

# 生成可行的node候选集
def get_proper_nodes(current_node):
    temp = []
    if is_good(current_node.x,current_node.y-1):
        temp.append((current_node.x,current_node.y-1))
        
    if is_good(current_node.x,current_node.y+1):
        temp.append((current_node.x,current_node.y+1))

    if is_good(current_node.x+1,current_node.y):
        temp.append((current_node.x+1,current_node.y))

    if is_good(current_node.x-1,current_node.y):
        temp.append((current_node.x-1,current_node.y))
    return temp

# 获取node对象列表中的坐标值列表
def waited_nodes(open):
    node_list = []
    for node in open:
        node_list.append((node.x,node.y))
    return node_list


node_cat = Node(cat_x,cat_y)
node_cat.G = 0
node_cat.H = get_instance(cat_x,cat_y)
node_cat.F = node_cat.G + node_cat.H
open.append(node_cat)

while True:
    print("候选点：",waited_nodes(open))
    current_node = get_node_with_MinFValue(open)
    print("选择的下一个点:",(current_node.x,current_node.y))
    print("\n")
    closed.append((current_node.x,current_node.y))
    open.remove(current_node)
    if (bone_x,bone_y) in closed: # 已找到路径
        break
    proper_node = get_proper_nodes(current_node)
    if len(proper_node) > 0:
        for (x,y) in proper_node:
            temp_node = Node(x,y)
            temp_node.G = current_node.G + 1
            temp_node.H = get_instance(x,y)
            print("({},{}).G:{}".format(x,y,temp_node.G))
            print("({},{}).H:{}".format(x,y,temp_node.H))
            temp_node.F = temp_node.G + temp_node.H
            if temp_node not in open:
                open.append(temp_node)
            # if its already in the open list
			# test if using the current G score make the aSquare F score lower, 
            # if yes update the parent because it means its a better path
            else:
                print("已在open中的node:",(temp_node.x,temp_node.y))
            #     if temp_node.G<

    if len(open) == 0: # Continue until there is no more available square in the open list (which means there is no path)
        break
print("closed表：",closed)
closed_copy = closed[:]

# for i in range(len(closed_copy)-1):
#     if (abs(closed_copy[i][0]-closed_copy[i+1][0])+abs(closed_copy[i][1]-closed_copy[i+1][1]))>1:
#         closed.remove((closed_copy[i+1][0],closed_copy[i+1][1]))

# 倒序删除，解决长度变化问题
for i in range(len(closed_copy)-1,-1,-1):
    if (abs(closed_copy[i][0]-closed_copy[i-1][0])+abs(closed_copy[i][1]-closed_copy[i-1][1]))>1 and i>0:
        print(closed_copy[i-1])
        closed_copy.remove(closed_copy[i-1])
print("最短路径表：",closed_copy)
print("最短路径长度：",len(closed_copy))




