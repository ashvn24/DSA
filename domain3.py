#binary search tree

class binary():
    def __init__(self):
        self.root=None
        self.left=None
        self.right=None
        
    
    def insert(self,node):
        root=self.node
        if root is None:
            node.left=binary()
        node.right=None
        if node>root:
            if root.right is None:
                root.right=node
            else:
                node.right=binary()

    def preorder(self):
        if self.root is None:
            print("empty")
        else:
            print(self.root.data)
            
                
            