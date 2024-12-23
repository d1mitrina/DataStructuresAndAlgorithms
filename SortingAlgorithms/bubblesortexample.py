bubble_list = [3,445,6,3,356,63]

for i in range(0,len(bubble_list)):
    for j in range(i,len(bubble_list)):
        if bubble_list[i]>bubble_list[j]:
            bubble_list[i],bubble_list[j] = bubble_list[j],bubble_list[i]

print(bubble_list)
