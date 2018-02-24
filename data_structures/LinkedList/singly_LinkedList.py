class Node:  # create a Node
    def __init__(self, data, nextnode=None):
        self.data = data  # given data
        self.nextnode = nextnode  # given nextnode to None
        
class Linked_List:
    def __init__(self,header=Node(None)):
        self.header=header
                 
    def insert_tail(self, tmpnode):
        tmp=self.header
        while not(tmp.nextnode==None):
            tmp=tmp.nextnode
        tmp.nextnode=tmpnode

    def insert_afterheader(self, tmpnode):
        tmp=self.header.nextnode
        self.header.nextnode=tmpnode
        tmpnode.nextnode=tmp

    def printList(self):  # print every node data
        tmp = self.header.nextnode
        while tmp is not None:
            print(tmp.data)
            tmp = tmp.nextnode
