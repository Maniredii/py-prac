

#TOPICS AVAILABLE 
# 1. ARMSTRONG NUMBER
# 2. SPY
# 3. sTRONG
# 4. PERFECT
# 5. HARSHAD
# 6. NEON


#------ ARMSTRONG NUMBER
# --- count how many steps are there
# --- access all the digits one by one
# --- calculate digit digit count and store it inside a var
# --- 

original_num = 153
# num = original_num
# temp = original_num
# digit_count = 0
# add = 0
# while num != 0:
#     num = num // 10
#     digit_count += 1
# while temp != 0:
#     last_digit = temp%10
#     add += last_digit ** digit_count
#     temp = temp // 10
# if original_num == add:
#     print("Armstrong num")
# else:
#     print("not armstrong num")



# Armstrong number check in Python

# num =   153       #int(input("Enter a number: ")) 
# sum = 0
# temp = num

# while temp > 0:                   # temp value = 15 
#     digit = temp % 10             # -- 3  15 % 10 = 5 
#     sum += digit ** 3             # cube of each digit sum = sum + digit ** 3 0 + 3 ^3 = 27 ||   
#     temp //= 10                   # temp = temp // 10 153 last num remove == 15 

# if num == sum:
#     print(num, "is an Armstrong number")
# else:
#     print(num, "is not an Armstrong number")



# ----- 

# num = 123
# sum = 1 + 2 + 3
# prod = 1 * 2 * 3
# if sum == prod:
#     print("equal")
# else:
#     print("not equal")



# --------------------- STRONG NUMBER   -------------------

# ori_num = 145
# num = ori_num
# add = 0
# while num != 0:
#     last_digit = num % 10
#     fact = 1
#     for i in range(2, last_digit+1):
#         fact = fact*i
#     add = add+fact
#     num //= 10
# if ori_num == add:
#     print("strong num")
# else:
#     print("not a strong num")




#----------- perfect 
# 1. use one loop to access the numbers from 1 to (n-1)
# 2. check wether the number is properly divisible by the i value or not 
# 3. if divisible add them and store inside a variable
    
# a number which is equal to the sum of its proper positive divisor 
# ex : 6--- /6 is divisible by 1, 2, 3

# num = 5
# add = 0
# for i in range(1, num):
#     if num % i == 0:
#         add = add + i
# if num == add:
#     print("perfect number")
# else:
#     print("not a perfect number")


# ---------- harshad 

# HARSHAD NUMBER IS COMPLETELY DIVISIBLE BY THE SUM OF ITS DIGITS 

# num = 18
# find out the sum of digits, sum of digits = 1 + 8 = 9
# check wether the num is properly divisible by sum of digit or not

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


# ------- NEON NUMBER

#A SPECIAL NUMBER WHERE THE SUM OF THE DIGITS OF ITS SQUARE IS EQUAL TO THE ORIGINAL NUMBER ITSELF

#FIND THE SQUARE OF THE NUMBER
# SUM OF DIGITS OF SQUARE  SUM = 1 + 8 = 9
# IF NUM == SUM THEN NEON NUMBER


# num = 9
# square = num**2
# add = 0
# while square != 0:
#     last_digit = square%10
#     add = add + last_digit
#     square //= 10
# if num == add:
#     print("neon number")
# else:
#     print("not a neon number")


