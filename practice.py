#check string number
# a number is called a strong number if the sum of the factorials of its digits is equal to the number it self
# input = 145
# o/p : strong number

# n = int(input("enter a number: "))
# num = n
# add = 0
# while num != 0:
#     digit = num % 10
#     fact = 1
#     for i in range(2, digit+1):
#         fact *= i 
#     add += fact
#     num //= 10
# if n == add:
#     print("strong number")
# else:
#     print("not a string num")


# check harshad number 

# num = 18
# temp = num
# digit = 0

# while temp > 0:
#     digit = digit + temp % 10
#     temp = temp // 10
# if num % digit == 0:
#     print("yes")
# else:
#     print("no")



# check neon number
# ----- a num is called neon number if the sum of the digits of its square is equal to the number it self

# num = 9
# square = num**2
# add = 0
# while square != 0:
#     last_digit = square%10
#     add = add + last_digit
#     square //= 10
# if num == add:
#     print("neon")
# else:
#     print("not neon")



# check perfect number
# a number is called perfect number if the sum of its proper divisors equals to the number

#find sum of digits 
#write a program to find the sum of all digits in a given number

#Reverse a number 
#write a program to reverse a digits of a given number

