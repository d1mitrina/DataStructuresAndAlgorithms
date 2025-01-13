#First IN, First OUT FIFO

class Queue():
    def __init__(self,size):
        self.size = size
        self.queue = [None] * size #it will create a list with an empty slot
        self.front = 0
        self.rear = 0
        self.available = size #how many slots are empty 


    def enqueue(self,item):
        if self.available == 0: #checks if there are no available slots
            print("Cannot add more items, queue is full! ")
        else:
            self.queue[self.rear] = item
            self.rear+=1 #places position on rear position
            self.available-=1
        
    def dequeue(self):
        if self.available == self.size:
            print("The queue is empty! ")
        else:
            removed_item = self.queue[self.front]
            self.queue[self.front] = None #means if first item is removed, then the first slot would be empty 
            self.front+=1
            self.available+=1
            print("The first item is removed")
        
    def get_front(self):
        if self.available == self.size: 
            print("The queue is empty! ")  #returns first item in the list
        else:
            print(self.queue[self.front])
        
    def get_rear(self):
        if self.available == self.size:
            print("The queue is empty! ") #returns last item in list
        else:
            print(self.queue[self.rear])
        
    def print_queue(self):
        print(self.queue)

myQueue = Queue(5)
myQueue.enqueue(2)
myQueue.enqueue(8)
myQueue.enqueue(1)
myQueue.enqueue(9)



myQueue.printQueue()


    

























