#LIFO - Last In, First Out LIFO

class Stack():
    def __init__(self,n): #n denotes MAX number of items in a stack 
        self.stck = []
        self.n = n

    def push(self,item_to_be_added):
        if len(self.stck) < self.n:
            self.stck.append(item_to_be_added)
        else:
            print("Stack is full, item cannot be added")
    
    def pop(self):
        if len(self.stck) == 0:
            print("Stack is empty")
        else:
            self.stck.pop(-1)
        
    def top(self): #gets the content of the last item. takes the value
        if len(self.stck) == 0:
            print("Stack is empty")
        else:
            return self.stck(-1)
    
    def size(self):
        return len(self.stck)
    
    def display(self):
        print(self.stck)

    
x = Stack(5)
x.display()
print(x.size())

x.push(3)
x.display()
print(x.size())

x.push(5)
x.display()
print(x.size())

x.push(2)
x.display()
print(x.size())

x.push(9)
x.display()
print(x.size())

x.push(1)
x.display()
print(x.size())

x.push(20)
x.display()
print(x.size())

x.pop()
x.display()
print(x.size())




