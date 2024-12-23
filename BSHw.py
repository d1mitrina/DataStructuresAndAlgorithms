def binarySearch(numbers,start_index,end_index,search_key):
    middle = (start_index + end_index)
    middle = middle // 2
    if start_index<=end_index : 
        if numbers [middle] == search_key:
            return middle
        elif numbers[middle]<search_key:
            return binarySearch(numbers,middle+1,end_index,search_key)
        else:
            return binarySearch(numbers,start_index,middle-1,search_key)
    else:
        return -1 


numbers = []
num_of_items = int(input("How many items do you want in the list? "))

for i in range(num_of_items):
    a = int(input("Enter number: ")) 
    numbers.append(a)


searchKey = int(input("Enter which key you want to search: "))

print(binarySearch(numbers,numbers[0],numbers[-1],searchKey))
