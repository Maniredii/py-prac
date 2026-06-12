# petrol pump fuel filling vehicles arrive one by one at a petrol station record fuel filled for each vehicle 
# until the total fuel reaches 500 liters


# fuel = 500.0
# vehicles = 0
# while fuel > 0:
#     fill = float(input("Enter the fuel filled in vehicle : "))
#     if fuel >= fill:
#         rem_fuel = fuel - fill
#         print(f"you used {fill} and you have {rem_fuel} remaining")
#         fuel = rem_fuel
#         vehicles+= 1
#     elif rem_fuel <= 0:
#         print("fuel is over")
#         break
#     else:
#         fuel.append(fill)
# print(f"fuel filled for each vehicle until 500 liters and remaining fuel is {fuel} ")
# print(f"total vehicles filled 500 liters : {vehicles}")



#hospital patient temperature check : a hospital records temperature of patients entering the emergency ward stop when a patient with temperature
# above 104f is found and display the patient count checked before that 

# count = 0
# while True:
#     temp = int(input("Enter the temperature of the patient : "))
#     if temp < 104:
#         count = count+1
#     else:
#         break
# print(f"total patient entered into ward is {count}")



# website login attempt system :  a user has only 3 attempts to enter the correct password display access granted 
# if correct other wise block the account

# count = 0
# password = input("enter your password : ")
# while count > 3:

#     if password == "pass@123":
#         print("Access Granted")
#         break
#     else:
#         count = count + 1
#         print(f"invalid password you have {2-count} attepmts left")
# if count >= 3:
#     print("account blocked")

# psd = '1234'
# i = 1
# while i <= 3:
#     pas = input("Enter your password : ")
#     i+= 1
#     if psd == pas:
#         print("access granted")
#         break
#     else:
#         print("try again")
#         print(f"remaining attempts {3 - i+1}")
# else:
#     print("Acount blocked")


# a student enters marks for subjects one by one print how many times the marks increased compared to the previous subject

# marks = []
# count = 0
# for _ in range(5):
#     mark = int(input("Enter your marks : "))
#     if marks == 0:
#         print("no comparison possible")
#     elif mark > marks[-1]:
#         count += 1
#         print("your marks changed")
#     else:
#         print("no changes in your marks ")



# n = int(input("enter no.of subjects "))
# prev = int(input("Enter your marks : "))
# i = 1
# count = 0
# while i <= n-1:
#     mark = int(input("Enter your next marks : "))
#     if mark > prev:
#         count += 1
#     prev = mark
#     i += 1
# print("the increase of marks with prev marks is ", count)


'''
 write a program that keeps asking the user for a number until they enter 0, then prints the sum of all entered numbers
sum = 0
while True:
    num = int(input("Enter a number : "))
    if num == 0:
        break
    else:
        sum = sum + num
print(sum)

'''


'''
# sum of the digits until single digit keep summing the digits of a number until the result is a single digit.
# example 98765 = 9+8+7+6+5 = 35 - 35 = 3+5 

n = int(input("Enter your num : "))
while n > 9:
    total = 0
    while n > 0:
        total = total + n % 10
        n = n //10
    n = total
print(n)

'''


'''
start with any positive integer N. if even divide by 2 if odd multiple by 3 and add 1 repeat until you reach 1 print the sequence length

'''
# length = 0
# n = int(input("Enter your number"))
# while n != 0:
#     if n % 2 == 0:
#         n = n //2
#     else:
#         n = n* 3 + 1
#     print(n)
# print(n)
# print(length)


'''
generate the first 20 terms of the fibonacci sequence using a loop 

'''

# n = 20



'''
# simulate a simple lottery : generate a random number between 1 and 20 (hardcode for testing or use random) 
# allow the user to guess 5 times. after each guess tell ig they are correct or not if correct print you win and exit the loop 
# if all 5 guesses are wrong you lose the number was " "

import random
win_num = random.randint(1, 20)
guesses = 0
while guesses < 5:
    guess = int(input("Enter guess num(1-20): "))
    if guess == win_num:
        print("you win")
        break
    else:
        print("sorry you loose")
    guesses += 1
if guesses >= 5:
    print(f"you loose the number are {win_num}")
'''

