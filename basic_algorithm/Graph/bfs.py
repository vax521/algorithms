import collections

def bfs(G,s):
    #P为记录每一个节点的父节点的字典
    P = {s:None}
    Q = collections.deque()
    Q.append(s)
    while Q:
        # print(Q)
        u = Q.popleft()
        for node in G[u]:
            if node in P.keys():
                continue
            # print(P.get(node,u))
            P[node]=P.get(node,u)
            Q.append(node)       
    return P

G={
    'a':{'b','f'},
    'b':{'c','d','f'},
    'c':{'d'},
    'd':{'e','f'},
    'e':{'f'},
    'f':{}
}

P=bfs(G,'a')
print(P)

#获取a至e的路径
u='f'
path=[u]
while P[u] is not None:
    path.append(P[u])
    u=P[u]
path.reverse()
print(path)