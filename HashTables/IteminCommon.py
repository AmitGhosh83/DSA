def repeating_item(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    for j in list2:
            # lookup j in dict
            if j in my_dict:
                 return True
    return False

list1 = [1,3,5]
list2 = [2,4,5]   

print(repeating_item(list1, list2))
# Use the Dictionary Key as the lookup value
# thats constant time