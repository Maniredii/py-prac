

# ---- square pattern


# for i in range(3):
#     print('* ' * 3)

# for i in range(2):
#     print("*", end = " ")  # print on same line


# for i in range(2):
#     print("* " *2) # prints 2 * 2 


# for i in range(1, 4):
#     print(i * 111)



# n = int(input("enter a number : "))
# for i in range(n):
#     print((str(i + 1) + " ")* n)


# WAP TO PRINT THE AAAA, (next line)BBB, CCC

# --- TO MAKE IT DYNAMIC TAKE THE INPUT FORM THE USER  

# for i in range(3):
#     print((chr(65 + i) + ' ') * 3)  # after the value change to 66 --- 67 

# n = 3
# for i in range(n):
#     print((str(i + 1) + ' ') * n)


#   WAP TO PRINT 123, /N 123, /N 123

# for j in range(3):
#     for i in range(3):
#         print(i+1, end = ' ')
#     print()


# WAP TO TO PRINT 1 2 3 /N 4 5 6 /N 7 8 9


# n = 1
# for i in range(3): # in place of 3 we can take custom input by creating input function
#     for j in range(3):
#         print(n, end = ' ') # first it will print 1 2 3 and later it will go to other line n = n + 1 and n value will be increased and later it will perform others
#         n = n +1
#     print()



# ----- WAP TO PRINT A B C /N D E F /N G H I


# n = 65
# #chr(n)
# for i in range(3):
#     for j in range(3):
#         print(chr(n), end = ' ')  # it will convert the number into ascii values 
#         n = n + 1
#     print()



# -------------- TRIANGLE PATTERNS ---------------

# -------------- TRIANGLE PATTERNS ---------------


# two for loops for triangle pattern
#n = 4
# for i in range(1, 5):
#     for j in range(i):
#         print('*', end = ' ')
#     print()


#-- same as above one 
# --------- single line for loop for triangle pattern =
# for i in range(3):
#     print("* " *(i + 1))


# for i in range(3):
#     for j in range(i + 1):
#         print("*", end = " ")
#     print()


# ------- WAP TO PRINT TRIANGLE NUMBER PATTERN

# num = int(input("enter your number : "))
# n = 1
# for i in range(num):
#     for j in range(i+1):
#         print(n, end = " ")
#         n = n + 1
#     print()


# WAP TO PRINT ALPHABETS IN TRIANGLE PATTERN

# num = int(input("Enter your number : "))
# n = 97  # it prints small alphabets 
# for i in range(num):
#     for j in range(i + 1):
#         print(chr(n), end = " ")
#         n = n + 1
#     print()


# ---- WAP TO PRINT REVERSE TRIANGLE

# n = 3
# for i in range(3):
#     print(('  ' * (n - 1 - i)) + ('* ' * ( i + 1)))




#***
#**
#*

# if i = 0 stars = 3 = n - i, if i = 1 stars = 2 n - i , if i = 2 stars = 1 n = i 
# n = 3
# for i in range(3):
#     print('*' * (n - i))


# ***
#  **
#   *

# if i = 0 stars = 3 == n - i, spaces = 0

n = 4
for i in range(n):
    print(('  '*i) +('* ' *(n - 1 - i)))
