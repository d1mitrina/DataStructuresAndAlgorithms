#graphs represent connections between different nodes in cs 

class Graph():
    def __init__(self):
        self.pathways = {}
    def add_roads(self,city1,city2):
        self.pathways[city1] = [] #there is no value  
        self.pathways[city2] = []
        self.pathways[city1].append(city2)
        self.pathways[city2].append(city1)
    def ShowGraph(self):
        for i,j in self.pathways.items(): # i reffering to city and j reffering to other city it is connected to 
            print (i,"is connected to",j)


cities = Graph()
cities.add_roads("London","Paris")
cities.add_roads("Paris","Zurich")
cities.add_roads("Zurich","Rome")
cities.add_roads("Rome","London")

cities.ShowGraph()






            