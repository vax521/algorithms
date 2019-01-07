# 二叉搜索树
class BST:
    class Node:
        def __init__(self,key,value):
            self.key = key
            self.value = value
            self.left_node = self.right_node = None

    def __init__(self):
        self.__root = None
        self.__count = 0

    def get_size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0
    
    def insert(self,key,value):
        self.__root = self.__insert(self,self.__root,key,value)
        