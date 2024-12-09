def fibonacci(n):
    if n == 0 or n==1:
        return n 
    else:
        return fibonacci(n-1) + fibonacci(n-2) #calling function inside --> recursions
    
for i in range(10):
    print (fibonacci(i))


#write code for factorial 
