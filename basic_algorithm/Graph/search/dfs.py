 # 深度优先遍历
 # 递归版
 ##G表示要遍历的图，s表示当前节点，points表示遍历过的节点集合，results表示结果
def recursive_dfs(G,s,points=None,results=None):
    if points is None:
        points = set()
    if results is None:
        results = []
    results.append(s)
    points.add(s)
    for node in G[s]:
        if node in points:
            continue
        points.add(node)
        # print(node)
        recursive_dfs(G,node,points,results)
    return results

# 迭代版dfs:
def iter_dfs(G,s):
    Q = []
    S = set()
    Q.append(s)
    while Q:
        # 当前节点
        node = Q.pop()
        if node in S:
            continue
        S.add(node)
        # 将邻接点列表加入Q
        Q.extend(G[node])
        yield node


if __name__ == '__main__':
    #有向无环图的邻接字典
    G={
        'a':{'b','f'},
        'b':{'c','d','f'},
        'c':{'d'},
        'd':{'e','f'},
        'e':{'f'},
        'f':{}
    }
    # res=recursive_dfs(G,'a')
    # print(res)
    print(list(iter_dfs(G,'a')))
