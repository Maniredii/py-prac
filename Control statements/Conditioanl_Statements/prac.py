# 1. Write a program to find the larger of two numbers and three numbers.
# num1 = input("Enter your first num : ")
# num2 = input("Enter your second num : ")
# num3 = input("Enter your third num : ")
# if(num1 > num2):
#     print(num1, "is grater")
# elif(num2 > num3):
#     print(num2, "is geater")
# elif(num3 > num1):
#     print(num3, "is greater")

#2. Write a program to check whether a number is divisible by both 2 and 3.

# num = int(input("enter your num : "))
# if num % 3 == 0 & num % 5 == 0:
#     print("num is divisible by both")
# elif num % 3 == 0:
#     print("num divisible by 3")
# elif num % 5 == 0:
#     print("num divisible by 5")
# else :
#     print("num is not divisible by both")



#3. Write a program to check whether a given alphabet is uppercase or lowercase.
# alpha = input("enter your character : ")
# if 'A' <= alpha <= 'Z':
#     print("upper case")
# elif 'a' <= alpha <= 'z':
#     print("lower case")


#4. Write a program to calculate bonus: Salary above 50,000 → 10% bonus Otherwise → 5% bonus
# sal = int(input("Enter your sal : "))
# if sal > 50000:
#     bonus = sal*0.1
#     print(bonus)
# else: 
#     bonus = sal*0.05
#     print(bonus)

#5. Write a program to check whether a number is a multiple of 7.
# num = int(input("enter your num : "))
# if num % 7 == 0:
#     print("num is divisible by 7")
# else:
#     print("num is not divisible by 7")


# 6. Write a program to display grades based on marks:
#     90–100 → A
#     75–89 → B
#     50–74 → C
#     Below 50 → Fail

# marks = float(input("enter your marks : "))
# if marks >= 90 and marks <= 100:
#     print("your grade is A")
# elif marks >= 75 and marks < 90:
#     print("Your grade is B")
# elif marks >= 50 and marks < 75:
#     print("your grade is C")
# else :
#     print("you are failed")



# 7. Write a calculator program using elif for:
#     Addition
#     Subtraction
#     Multiplication
#     Division

# num1 = float(input("enter your first num : "))
# num2 = float(input("enter your second num : "))
# operator = input("Enter your operator : ")
# if operator == "+":
#     print(num1 + num2)
# elif operator == "-":
#     print(num1 - num2)
# elif operator == "*":
#     print(num1 * num2)
# elif operator == "/":
#     print(num1 / num2)