# 所以邻接字典做了特殊的约定，每一个节点所能访问到的节点（直接或间接）
# 均显示在该节点的集合
# 使用的图为 test.webp
# 关键是维护一个入度为零的定点集合

# def topoSort(G,S=None):
#     if S is None:
#         S = set(G.keys())
#     if len(S)==1:
#         return list(S)
#     s = S.pop()
#     seq = topoSort(G,S)
#     minIdx = 0
#     for i,v in enumerate(seq):
#         if s in G[v]:
#             minIdx = i+1
#     seq.insert(minIdx,s)
#     return seq

def naiveTopoSort(G):
    # 保存各个节点的入度的字典
    in_dgree = {}
    for key in G.keys():
        in_dgree[key]=0

    # 计算入度
    for key in G.keys():
        for item in G[key]:
            in_dgree[item] += 1
    # 打印各个节点的入度
    # for key,value in in_dgree.items():
    #     print(key,value)       

    # 入度为零的节点
    in_degree_0 = []
    for key in G.keys():
        if in_dgree[key] == 0:
            in_degree_0.append(key)
    print("in_degree_0:",in_degree_0)

    result = []
    while len(in_degree_0) > 0:
        # p出队
        p = in_degree_0.pop()
        result.append(p)
        print("G[p]:",G[p])
        for k in G[p]:
            # 对应节点入度减一
            in_dgree[k] = in_dgree[k]-1
            if in_dgree[k] == 0:
                in_degree_0.append(k)
    return result

#有向无环图的邻接字典  
G={
    'a': {'b','c','d','e','f'},
    'b': {'c','d','e','f'},
    'c': {'d','e','f'},
    'd': {'e','f'},
    'e': {'f'},
    'f': {}
}

res = naiveTopoSort(G)
print(res)

