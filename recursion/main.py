#WAP USING RECURSION TO FIND THE SUM OF N NUMBERS

#normal while loop
# n = int(input("Enter your num: "))
# total = 0
# i = 1
# while i <= n:
#     total = total + i
#     i = i + 1
# print(total)

# using recursion

# # n = int(input())
# def addNums(n, i = 1, add = 0):
#     if i > n:
#         return add
#     add = add + i
#     i = i + 1
#     return addNums(n, i, add)
# print(addNums(int(input("Enter a num: "))))



# WAP USING RECURSION TO FIND THE PRODUCT OF n NUMBERS

# WAP USING RECURSION TO FIND THE FACTORIAL OF A NUMBER

#WAP USING RECURSION TO FIND OUT THE NON REPEATING VALUE PRESENT INSIDE A LIST COLLECTION
# INPUT = ['HI', 1, 2, 1, 56, 20]
# OUTPUT = ['HI', 2, 56, 20]

# list = eval(input("Enter your list : "))
# i = 0
# unique_value = []
# while i < len(list):
#     if list.count(list[i]) == 1:
#         unique_value.append(list[i])
#     i += 1
# print(unique_value)

# RECURSION 

# def unique(coll, i = 0, unique_values=[]):
#     if i >= len(coll):
#         return unique_values
#     if coll.count(coll[i]) == 1:
#         unique_values.append(coll[i])
#     i+=1
#     return unique(coll, i, unique_values)
# # print(unique(['HI', 1, 2, 1, 56, 20]))
# print(unique(eval(input("Enter a list of values : "))))


#### WAP USING RECURSION TO FIND THE MAXIMUM NUMBER FROM A LIST COLLECTION
# coll = [5, 3, 1, 6, 9]
# i = 0
# max = coll[0]
# while i < len(coll):
#     if coll[i] > max:
#         max = coll[i]
#     i += 1
# print(max)

# Recursion

# def max(coll, i = 0, max_num = float('-inf')):
#     if i >= len(coll):
#         return max_num
#     if coll[i] > max_num:
#         max_num = coll[i]
#     i += 1
#     return max(coll, i, max_num)
# print(max(eval(input("Enter a list of numbers : "))))

# WAP USING RECURSION TO FIND THE MINIMUM NUMBER FROM A TUPLE COLLECTION


