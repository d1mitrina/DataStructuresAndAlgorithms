#N dimmesional tree - Where root node is A and sub nodes are B,C AND D

class TreeNode():
    def __init__(self,data):
        self.data = data
        self.children = []
root = TreeNode("a")
nodeB = TreeNode("b")
nodeC = TreeNode("c")
nodeD = TreeNode("d")

#adding the variables into the list 
root.children.append(nodeB)
root.children.append(nodeC)
root.children.append(nodeD)

#fist root then children
def preorder_traversal(root):
    if root is None: #if root is emmpty, it will come out from the fucntions
        return 
    print(root.data)
    for i in root.children:
        preorder_traversal(i)

preorder_traversal(root)

print("   ")

#first children then root 
def postorder_traversal(root):
    if root is None: 
        return
    for i in root.children:
        postorder_traversal(i)
    print(root.data) 

postorder_traversal(root)






