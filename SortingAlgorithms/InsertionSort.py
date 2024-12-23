#ascedninf insertion sort
a = [32,4,5,53,2,4,556654,3]
for i in range(0,len(a)):
    min = 1
    location = -1 
    for j in range(i,len(a)):
        if min > a[j]:
            min = a[j] #value
            location = j #index
            a[j],a[i] = a[i],a[j]
print(a)