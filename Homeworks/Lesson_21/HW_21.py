class Node:

    def __init__ (self, data, next_node = None, prev_node = None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

class DoubleLinkedList:

    def __init__ (self, root=None, leaf=None):
        self.root = root
        self.leaf = leaf
        self.size = 0

    def add (self, data):
        new_node = Node (data)
        
        if self.root is None:
            self.root = self.leaf = new_node
            self.size += 1
        else:
            new_node.prev_node = self.leaf
            new_node.next_node = None
            self.leaf.next_node = new_node
            self.leaf = new_node
            self.size += 1

    def __repr__ (self):
        next_n = self.root
        res = ''

        while next_n:
            res += str (next_n.data) + ' <-> '
            next_n = next_n.next_node
        return res


my_list = DoubleLinkedList()
my_list.add(5)
my_list.add(9)
my_list.add(7)
print (my_list)

