class Graph():
    def __init__(self):
        self.connections = {}
    def networks (self,net1,net2):

        if net1 not in self.connections:
            self.connections[net1] = [] 
        if net2 not in self.connections:
            self.connections[net2] = []
    
        self.connections[net1].append(net2)
        self.connections[net2].append(net1)
    def ShowGraph(self):
        for i,j in self.connections.items():
            print(i,"Is a connected to ",j)


connect = Graph()
connect.networks("A","B")
connect.networks("O","D")
connect.networks("F","D")
connect.networks("V","A")
connect.networks("J","E")
connect.networks("L","B")

connect.ShowGraph()


        