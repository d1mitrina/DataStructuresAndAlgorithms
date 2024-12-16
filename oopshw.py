class Cat():
    def __init__(self,colour,fur,size):
        self.colour = colour
        self.fur = fur 
        self.size = size
    def isMeowing(self):
        print("Cat is meowing")
    def notMeowing(self):
        print("Cat is not meowing")

cat1 = Cat("Black","Rough","Medium")

print(cat1.colour)

cat1.isMeowing()

class Kitten(Cat):
    def __init__ (self,colour,fur,size,height,width):
        Cat.__init__(self,colour,fur,size)
        self.height = height
        self.width = width
        
kitten1 = Kitten("brown","soft","small","5 inches","5 inches")
 
 
print(kitten1.colour,kitten1.fur,kitten1.size)