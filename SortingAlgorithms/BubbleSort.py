a = [1,3,4,42,3,444,23,4,5667676,0]
a.sort(reverse = True) #decsending order
print(a)
a.sort() 
print(a) #ascedending order


b = [1,3,4,42,3,444,23,4,5667676,0] #sample list

#descening algorithm 
length = len(b)
for i in range(0,length):
    for j in range(i,length):
        if b[i] < b[j]:
            b[i],b[j] = b[j],b[i]
print(b)
        
#asceding algorithm
length = len(b)
for i in range(0,length):
    for j in range(i,length):
        if b[i] > b[j]:
            b[i],b[j] = b[j],b[i]
print(b)
        