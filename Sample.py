# def print_items(n):
#     for i in range(n):
#         for j in range(n):
#           print(i,j)
# print_items(9)  

# n1= 11
# n2=n1

# print("before update")
# print("n1:",n1,id(n1))
# print("n2:", n2, id(n2))

# n2=22

# print("\nafter update 1")
# print("n1:",n1,id(n1))
# print("n2:", n2, id(n2))

# n1=n2

# print("\nafter update 2")
# print("n1:",n1,id(n1))
# print("n2:", n2, id(n2))

dict1={
    "value":11
}
dict2= dict1
print(dict1, id(dict1))
print(dict2, id(dict2))

dict2={
    'value':12
}
print("\n After update")
print(dict1, id(dict1))
print(dict2, id(dict2))