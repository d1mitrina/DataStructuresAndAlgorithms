
class Graph():
    def __init__(self):
        self.pathways = {}
    def friends(self,friend1,friend2):
        if friend1 not in self.pathways:
            self.pathways[friend1] = [] 
        if friend2 not in self.pathways:
            self.pathways[friend2] = []


        self.pathways[friend1].append(friend2)
        self.pathways[friend2].append(friend1)
    def ShowGraph(self):
        for i,j in self.pathways.items(): 
            print (i,"is friends with",j)


cities = Graph()
cities.friends("Lilia","Alyssa")
cities.friends("Alyssa","Maya")
cities.friends("Maya","Phoebe")
cities.friends("Lilia","Mia")
cities.friends("Lilia","Bob")
cities.friends("Bob","Bart")



cities.ShowGraph()

