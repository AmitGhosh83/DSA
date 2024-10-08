def merge(list1, list2): 
    combined = []
    i = 0
    j = 0
    
    while (i < len(list1) and j < len(list2)): 
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
            combined.append(list1[i])
            i += 1
    while j < len(list2):
            combined.append(list2[j])
            j += 1 
    return combined

def merge_sort(inputlist):
     if len(inputlist) == 1:
          return inputlist
     
     mid_index = len(inputlist)//2
     left = merge_sort(inputlist[: mid_index])
     right = merge_sort(inputlist[mid_index:])
     sorted_list = merge(left,right)
     return sorted_list 
    

# list1 = [1,3,5,7]
# list2 = [2,4,6,8]
input_list = [3,1,2,7]

# print(merge(list1, list2))  
print (merge_sort(input_list))           