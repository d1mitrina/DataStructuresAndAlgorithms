class TreeNode():
    def __init__(self,data):
        self.data = data
        self.children = []

root = TreeNode(1)
num2 = TreeNode(2)
num3 = TreeNode(3)
num4 = TreeNode(4)
num5 = TreeNode(5)
num6 = TreeNode(6)
num7 = TreeNode(7)


root.children.append(num2)
root.children.append(num3)
root.children.append(num4)
num2.children.append(num5)
num2.children.append(num6)
num3.children.append(num7)

def preorder_traversal(root):
    if root is None: 
        return 
    print(root.data)
    for i in root.children:
        preorder_traversal(i)

preorder_traversal(root)

