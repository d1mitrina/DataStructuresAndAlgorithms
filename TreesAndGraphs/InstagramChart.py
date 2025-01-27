class TreeNode():
    def __init__(self,name):
        self.name = name
        self.friends = []
    def adding(self,friend):
        self.friends.append(friend)
    def display(self,level = 0):
        print(" " * level * 2+self.name)
        for i in self.friends:
            i.display(level+1)

User = TreeNode("Dimitrina")
friend1 = TreeNode("Alyssa")
friend2 = TreeNode("Bob")
friend3 = TreeNode("Eva")
friend4 = TreeNode("Holly")

User.adding(friend1)
User.adding(friend2)
friend1.adding(friend3)
friend2.adding(friend4)

User.display()
