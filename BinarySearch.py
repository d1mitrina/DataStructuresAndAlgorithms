#binary search can only be applied in sorted lists / data (ascending order)
#faster, more efficient than linear search 

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

print(binarySearch([1,5,6,7,8,99],0,5,8))