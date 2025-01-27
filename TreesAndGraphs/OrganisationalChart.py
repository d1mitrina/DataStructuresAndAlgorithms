class TreeNode():
    def __init__(self,name,position):
        self.name = name
        self.position = position 
        self.hierarchy = []
    def adding(self,child):
        self.hierarchy.append(child)
    def display(self,level = 0):
        print(" " * level * 2+self.name,self.position)
        for i in self.hierarchy:
            i.display(level+1)

ChairMan = TreeNode("Dimi","Chairman")
Ceo = TreeNode("Renuka","CEO")
HeadOfSales = TreeNode("David","HeadOfSales")
HeadOfMarketing = TreeNode("Jake","HeadOfMarketing")
SalesManager1 = TreeNode("Sophia","Sales Manager 1")
SalesManager2 = TreeNode("Mia","Sales Manager 2")
MarketingManager1 = TreeNode("Bob","Marketing Manager 1")
MarketingManager2= TreeNode("Bob","Marketing Manager 2")


ChairMan.adding(Ceo)
Ceo.adding(HeadOfSales) #adds child to parent) 
Ceo.adding(HeadOfMarketing)
Ceo.adding(HeadOfSales)
HeadOfMarketing.adding(MarketingManager1)
HeadOfMarketing.adding(MarketingManager2)
HeadOfSales.adding(SalesManager1)
HeadOfSales.adding(SalesManager2)

ChairMan.display()
