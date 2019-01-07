
class Node:
    def __init__(self,freq):
        self.left = None 
        self.right = None
        self.father = None
        self.freq = freq
    # 父节点的左节点是不是自己
    def is_left(self):
        return self.father.left == self

# 创建节点列表
def create_nodes(freqs):
    return [Node(freq) for freq in freqs]

# # 创建哈弗曼树
def create_huffman_tree(nodes):
    queue = nodes[:]
    while len(queue) > 1 :
        # 根据频率排序
        queue.sort(key=lambda item: item.freq)
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_father = Node(node_left.freq+node_right.freq)
        node_father.left = node_left
        node_father.right = node_right
        node_left.father = node_father
        node_right.father = node_father
        queue.append(node_father)
    queue[0].father=None
    print("root node:"+str(queue[0]))
    return queue[0]


# 创建编码
def huffman_encoding(nodes,root):
    codes = [''] * len(nodes)
    for i in range(len(nodes)):
        node_temp = nodes[i]
        # 从树底向上遍历
        while node_temp != root:
            if node_temp.is_left():
                codes[i] = '0' + codes[i]
            else:
                codes[i] = '1' + codes[i]
            node_temp = node_temp.father
    return codes

if __name__=="__main__":
    chars_freqs = [('C', 2), ('G', 2), ('E', 3), ('K', 3), ('B', 4),
                   ('F', 4), ('I', 4), ('J', 4), ('D', 5), ('H', 6),
                   ('N', 6), ('L', 7), ('M', 9), ('A', 10)]
    nodes = create_nodes([item[1] for item in chars_freqs])
    for node in nodes:
        print(node.freq)
    root = create_huffman_tree(nodes)
    codes = huffman_encoding(nodes,root)
    for item in zip(chars_freqs,codes):
        print('Character:%s freq:%-2d   encoding: %s' % (item[0][0],item[0][1],item[1]))