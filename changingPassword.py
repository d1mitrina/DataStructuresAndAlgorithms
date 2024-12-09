#print(type('jieifjj'))
#print(type(4.3345))

class User():
    __password="123Dimi" #hidden property / attribute for  added  security
    def __init__(self,name,email,username):
        self.name = name
        self.email = email 
        self.username = username
    
    
    
    def get_password(self): #getter functions can only be accessed by admin in real life. 
        return self.__password
    


    def set_password(self):
        original_pass= input("Enter your old password: ")
        if original_pass  == self.__password:
            new_pass = input("Enter new password: ") 
            self.__password = new_pass
        else:
            print("Please enter the correct original password")



dimi = User("Dimitrina","dimi@icloud","dimitrina123")
print(dimi.name,dimi.username,dimi.email)
#print(__password)
#print(dimi.__password) #'User' object has no attribute '__password'
print(dimi.get_password())

dimi.set_password()
print(dimi.get_password())
