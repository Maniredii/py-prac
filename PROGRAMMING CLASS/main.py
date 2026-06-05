# import math
# a = int(input('Enter coffiecient of xsqr: '))
# b = int(inout('enter coffiecient of x : '))
# c = int(input('enter constant: '))

# if a == 0:
#     if b == 0:
#         print('no solutions')
#     else:
#         root = -c/b
#         print('the root of e')
# else:
#     D = (b**2)-(a*a*c)
#     if D ==0:
#         root = (-b)/(2*a)
#         print('thje root of the quadratic equation is ', root)
#     elif D > 0:
#         root


# a vending machine accepts coins of rupe1, rup2, 
# a = int(input('enter your bill : '))
# b = int(input('enter amount paid : '))
# # c = b - a
# if b < a:
#     print(f"you paid rupees {a} amd need to pay more rupees {a - b}")
# elif b == a:
#     print("paid amount is equal to bill amount")
# else:
#     # print("paid amount is greater then bill amount please collect your change")
#     change = b > a
#     if change >= 500:
#         count = change//500
#         print(f'{count} x 500')
#         change = change % 500
#     if change >= 200:
#         count = change//200
#         print(f'{count} x 200')
#         change = change % 200
#     if change >= 100:
#         count = change//100
#         print(f'{count} x 100')
#         change = change % 100
#     if change >= 50:
#         count = change//50
#         print(f"{count} x 50")
#         change = change % 50
#     if change >= 20:
#         count = change//20
#         print(f"{count} x 20")
#         change = change % 20
#     if change >= 10:
#         count = change//10
#         print(f"{count} x 10")
#         change = change % 10
#     if change >= 5:
#         count = change//5
#         print(f"{count} x 5")
#         change = change % 5
#     if change >= 2:
#         count = change//2
#         print(f"{count} x 2")
#         change = change % 2
#     if change >= 1:
#         count = change//1
#         print(f"{count} x 1")
#         change = change % 1

    



#take a 3 digit number and print its digit in reverse order without using string slicing of loops 
# (use arithmetic conditions only) also check if the reversed number equals the original (palindrome)

# n = int(input('enter your number: '))
# num = n 
# ones = num % 10
# tens = (num//10)%10
# hund = num //100
# rev = ones*100 + tens*10+hund
# print(rev)
# if rev == num:
#     print("palindrome")
# else:
#     print('not palindrome')


#simulate a simple ATM transaction start with a balance of 5000 ask the user for an option 1. withdraw, 2. deposit, 3. check balance
# for withdraw, ask the amount if amount > balance, print insufficient funds false deduct and show new balance

# balance = 5000
# print("1. withdraw \n 2. deposit \n 3. check balance")
# choice = int(input("enter choice of(1-3) : "))
# if choice == 1:
#     amount = int(input("enter amount to withdraw : "))
#     if amount > balance:
#         print("insufficient balance")
#     else:
#         balance = balance- amount
#         print(f"you have {balance} remaining")
# elif choice == 2:
#     amount = int(input("enter your amount to deposit : "))
#     if amount <= 0:
#         print("Enter a correct amount")
#     else:
#         balance = balance + amount
#         print(f"your amount is deposited successfully and your total balance is {balance} ")
# elif choice == 3:
#     print(f"available balance is {balance}")
# else:
#     print("invalid choice")

    #
    # elancer



#-------------------------------01/06/

#a user enters a weekday(monday to sunday), if it is a weekday (mon-fri), ask for number of hours worked if hours > 40 pay = hours * 100
# + (hours-40)*50 (overtime). else pay = hours * 100. for weekdays (sat - sun), pay = hours *150 if entered invalid day print error print total pay
#

# print("1. Monday \n 2. Tuesday \n 3. Wednesday \n 4. Thursday \n 5. Friday \n 6. Saturday \n 7. Sunday")
# choice = input("Enter your choice in (1-7) : ")
# if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5':  # or if 
#     hours = float(input("Enter no.of hours worked : "))
#     if hours > 40:
#         pay = hours * 100 + (hours-40)*50
#         print(pay)
#     else:
#         pay = hours*100
#         print(pay)
# elif choice == '6' or choice =='7':
#     pay = hours * 150

# else:
#     print("enter a valid day")


#write a program that reads a 3 digit integer and prints whether the sum of the first and last digit equals the middle digit

# num = int(input("Enter a 3-digit integer: "))

# first_digit = num // 100
# middle_digit = (num % 100) // 10
# last_digit = num % 10

# if first_digit + last_digit == middle_digit:
#     print("The sum of the first and last digit equals the middle digit.")
# else:
#     print("The sum of the first and last digit does not equal the middle digit.")


# write a program that takes three integers and finds the second largest, do not use max()/min() or sorting
# use nested conditionals to compare values step by step

# num1 = input("enter num1 : ")
# num2 = input("enter num2 : ")
# num3 = input("enter num3 : ")
# if (num1 > num2) and (num1 > num3):
#     if(num2 > num3):
#         print("num2 is second largest ")
#     else:
#         print("num3 is second largest")
# elif (num2 > num1) and (num2 > num3):
#     if(num1 > num3):
#         print("num1 is second largest")
#     else:
#         print("num3 is second largest")
# elif (num3 > num1) and (num3 > num2):
#     if(num1 > num2):
#         print("num1 is second largest")
#     else:
#         print("num2 is second largest")




# create rock paper scissor 

import random

while True:
    user_move = input("Enter your move (rock/paper/scissors) or 'q' to quit: ").lower()
    if user_move == 'q':
        break
    com = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer's move: {com}")
    if user_move not in ['rock', 'paper', 'scissors']:
        print("Invalid input! Try again.")
        continue
    if user_move == com:
        print("It's a tie!")
    elif (user_move == 'rock' and com == 'scissors') or \
         (user_move == 'paper' and com == 'rock') or \
         (user_move == 'scissors' and com == 'paper'):
        print("You win this round!")
    else:
        print("Computer wins this round!")
        break

print("Thanks for playing! Goodbye.")

