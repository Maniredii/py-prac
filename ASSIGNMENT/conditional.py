#----------------------- 1--------------------



day = int(input("Enter no.of days late : "))
if day <= 5:
    total = day*2
    print(f"you return this book late in {day} so you got fine amount of {total}")

elif day >= 6 and day <= 10:
    total = day * 5
    print(f"you return this book late in {day} so you got fine amount of {total}")
elif day >= 11 and day <= 15:
    total = day * 10
    print(f"you return this book late in {day} so you got fine amount of {total}")
elif day > 15:
    total = day * 20
    print(f"you return this book late in {day} so you got fine amount of {total}")
    print("a warning letter has issued ")


# ----------------------------------- 2 --------------------------------------------


kills = int(input("Enter total number of kills : "))
death = int(input("Enter no.of time you died : "))
if kills < 5:
    score = kills * 100
    print(f"you got {kills} and your total score is {score}")
elif kills >= 5 and kills <= 10:
    score = kills * 150 + 500
    print(f"you got {kills} and your total score is {score}")
elif kills > 10:
    score = kills * 200 + 1500
    print(f"you got {kills} and your total score is {score}")
if death > kills:
    score /= 2
    print(f"your died {death} times more than your kills so your score will be deducted to {score}")


#------------------------------ 3 ------------------------------

age = int(input("enter Your age : "))
income = float(input("Enter your income : "))
if age >= 60 and income < 300000:
    print("no tax")
elif age >= 60 and income >= 300000 and income <= 500000:
    tax = income * 0.10
    print(f"your income is more than limit value so your should need to pay tax amount of {tax}")
elif age >= 0 and income > 500000:
    tax = income * 0.15
    print(f"your income is more than limit value so your should need to pay tax amount of {tax}")
elif age < 60 and income < 250000:
    print("no tax")
elif age < 60 and income >= 250000 and income <= 500000:
    tax = income * 0.05
    print(f"your income is more than limit value so your should need to pay tax amount of {tax}")
elif age < 60 and income >= 500000 and income <= 100000:
    tax = income * 0.20
    print(f"your income is more than limit value so your should need to pay tax amount of {tax}")
elif age < 60 and income > 1000000:
    tax = income * 0.30
    print(f"your income is more than limit value so your should need to pay tax amount of {tax}")

# ---------------------------------  4  -------------------------

metro_pins = ["400001", "110001", "700001"]
pin = input("Enter your pin code: ")
price = int(input("Enter product price: "))
weight = float(input("Enter order weight (kg): "))
if pin in metro_pins:  
    if price >= 1000:
        shipping = 0
    else:
        shipping = 40
else:  
    if price > 5000:
        shipping = 0
    elif weight <= 1:
        shipping = 60
    elif weight <= 5:
        shipping = 100
    else:
        shipping = 150 + (weight - 5) * 20
total = price + shipping
print(f"Shipping cost = ₹{shipping}")
print(f"Total price = ₹{total}")





#------------------------------------------ 5 -------------------

num = int(input("Enter a 4-digit number: "))
num_str = str(num)

if num_str == num_str[::-1]:
    if all(int(digit) % 2 == 0 for digit in num_str):
        print("Even palindrome")
    else:
        print("Mixed palindrome")
else:
    first_sum = int(num_str[0]) + int(num_str[1])
    last_sum = int(num_str[2]) + int(num_str[3])
    if first_sum == last_sum:
        print("Balanced number")
    else:
        print("Ordinary number")
