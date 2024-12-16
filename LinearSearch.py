#linear search is preferable for small sets of data
numbers = list(int(input("Enter the numbers: ").split())) #splitting numbers
search_key = int(input("Enter the search key"))

#first method IN (Linear Search)

if search_key in numbers: #IN key word -- > checking
    print("Number exists")


#second method FOR LOOP (Linear Search)

length = len(numbers)
for i in range (length):
    if numbers [i] == search_key:
        print("Number found")


#third method (Linear Search)

for i in numbers:
    if i == search_key:
        print("Number exists")


