#----------find the factorial of a number

# i = int(input("enter your num : "))
# fact = 1
# while i > 1: #here 5 will be the value of i and it will be decremented by 1 until it becomes 1
#     fact = fact*i 
#     i = i - 1 #here i value will be decremented by 1 until it becomes 1
# print(fact)

#-------- sum of numeric values of a cell
# address each value from the cell
# check wether the value is numeric or not
#if numeric add the numeric value to with existing sum

# coll = eval(input("enter your collection : "))
# add = 0
# i = 0
# while i < len(coll):
#     if type(coll[i]) in [int, float, complex]:
#         add = add+coll[i]
#     i = i+ 1
# print(add)


#------------ REVERSE A NUMBER


# num = int(input("Enter a number : "))
# rev = 0  #need to reverse the number
# while num > 0:
#     digit = num % 10  #accessing the last digit
#     rev = rev * 10 + digit 
#     num = num//10
# print(rev)


#----- wap to check wether a number is palindrome or not

# num = int(input("Enter your num : "))
# temp = num
# rev = 0

# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num//10
# if temp == rev:
#     print("palindrome")
# else :
#     print("not a palindrome")


# ------- wap to check wether a string is palindrome or not
