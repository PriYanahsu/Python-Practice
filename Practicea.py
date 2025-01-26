# def factorial(val, first, second):
#     list = []
#     list.append(first)
#     list.append(second)
#     for _ in range(val - 2): 
#         third = first + second
#         list.append(third)
#         second=third
#         first=second
#     return list

# list = factorial(5, 0, 1)
# for l in list:
#     print(l)


# find the number of odd number int the list and evven also

list = [1,2,3,4,5,6,7,8,9]
counteven = 0
countodd = 0
for l in list:
    if l % 2 == 0 :
        counteven+=1
    else:
        countodd+=1

print(countodd)
print(counteven)
        
