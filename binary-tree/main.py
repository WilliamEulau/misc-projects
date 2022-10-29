from datetime import datetime


class Node:
    def __init__(self,value = None, node_index = None):
        self.value=value
        self.node_index = node_index
        self.left=None
        self.right=None
        self.parent=None # pointer to parent Node in tree
        self.multiple = 1
        self.entrytime = None
        

class BST:
    def __init__(self):
        self.root=None
        self.node_index=0

    def insert(self, value):
        # Add a way to track entries to the tree. 
        if self.root == None:
            self.node_index = self.node_index + 1
            self.root = Node(value, self.node_index)
            self.root.entrytime = datetime.now().strftime("%Y:%m:%d:%H:%M:%S:%f")
        else:
            self._insert(value,self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left == None:
                self.node_index = self.node_index + 1
                cur_node.left = Node(value, self.node_index)
                cur_node.left.entrytime = datetime.now().strftime("%Y:%m:%d:%H:%M:%S:%f")
                cur_node.left.parent = cur_node # set parent
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right == None:
                self.node_index = self.node_index + 1
                cur_node.right = Node(value, self.node_index)
                cur_node.right.entrytime = datetime.now().strftime("%Y:%m:%d:%H:%M:%S:%f")
                cur_node.right.parent=cur_node # set parent
            else:
                self._insert(value,cur_node.right)
        else: 
            cur_node.multiple = cur_node.multiple + 1
            print(f"The value {value} is already in the tree, updated number of occurances: {cur_node.multiple}.")
    
    def MaxVal(self):
        if self.root == None: 
            print(f"The tree is empty")
        else: 
            return self._MaxVal(self.root)

    def _MaxVal(self, cur_node):
        if cur_node.right is None: 
            return cur_node.value
        else: 
            return self._MaxVal(cur_node.right)

    def MinVal(self):
        if self.root == None: 
            print(f"The tree is empty")
        else: 
            return self._MinVal(self.root)

    def _MinVal(self, cur_node):
        if cur_node.left is None: 
            return cur_node.value
        else: 
            return self._MinVal(cur_node.left)
    
    def TreeSum(self):
        return(sum(self.PrintTreeArray()))

    def TreeHeight(self): 
        if self.root == None: 
            return 0
        else: 
            return self._TreeHeight(self.root, 0)

    def _TreeHeight(self, cur_node, cur_height): 
        if cur_node == None: 
            return cur_height
        else:
            left_height = self._TreeHeight(cur_node.left, cur_height+1)
            right_height = self._TreeHeight(cur_node.right, cur_height+1)
            return max(left_height, right_height)

    def CountNodes(self):
        if self.root == None: 
            print(f"The tree is empty")
        else: 
            return len(self.PrintTreeArray())
    
    def PrintTreeArray(self):
        if self.root!=None:
            arr = []
            self._PrintTreeArray(self.root, arr)
            return arr

    def _PrintTreeArray(self,cur_node, array):
        if cur_node!=None:
            self._PrintTreeArray(cur_node.left, array)
            array.append(cur_node.value)
            self._PrintTreeArray(cur_node.right, array)

    def PrintTreeString(self):
        tree_str = ""
        arr = self.PrintTreeArray()
        for k in range(len(arr)): 
            tree_str = tree_str + " " + str(arr[k])
        return tree_str[1:]

    def RetrieveNode(self, value): 
        if self.root == None: 
            print("The tree is empty")
        elif self.root.value == value: 
            return self.root
        else: 
            return self._RetrieveNode(self.root, value)

    def _RetrieveNode(self, cur_node, value): 
        if cur_node.value == value: 
            return cur_node
        elif cur_node.value > value and cur_node.left: 
            return self._RetrieveNode(cur_node.left, value)
        elif cur_node.value < value and cur_node.right: 
            return self._RetrieveNode(cur_node.right, value)
        else: 
            print(f"The value {value} was not found in the tree")