

# -------------NESTED LOOP
'''
A finance company tracks daily profit and loss values for different departments.
Positive numbers represent profit
Negative numbers represent loss
Zero means no gain or loss
The manager wants to identify all unique groups of three departments where the total net result is zero. This means the profit and loss 
values balance each other perfectly.Task:
Write a Python program to find all unique triplets from the list whose sum is 0.Input:
A list of integers representing profit/loss values.
transactions = [-1, 0, 1, 2, -1, -4]Output:
All unique triplets whose sum is zero.
[[-1, -1, 2], [-1, 0, 1]]Explanation:
-1 + -1 + 2 = 0
-1 + 0 + 1 = 0
So these triplets balance to zero.

Example 2:Input:
transactions = [3, -2, -1, 0, 2, -3, 1]Output:
[[-3, 0, 3], [-2, -1, 3], [-3, 1, 2], [-2, 0, 2], [-1, 0, 1]]

Constraints:
Length of list ≥ 3
Values can be positive, negative, or zero
Return only unique triplets



transactions = [3, -2, -1, 0, 2, -3, 1]
res = []
for i in range(len(transactions)):
    for j in range(i+1, len(transactions)):
        for k in range(j+1, len(transactions)):
            if(transactions[i]+transactions[j]+transactions[k])==0:
                triplet = [transactions[i],transactions[j],transactions[k]]
                triplet.sort()
                if triplet not in res:
                     res.append(triplet)
    
    '''


# given a list of numbers and a target value find the paris of numbers whose sum is equal to target value

# numbers = [2, 4, 6, 8, 5, 3, 7, 9]
# target = 10
# i = 0
# while i < len(numbers):
#     j = i+1
#     while j < len(numbers):
#         if numbers[i] + numbers[j] == target:
#             print(numbers[i], "+", numbers[j], "=", target )
#         j = j + 1
#     i = i + 1


# find the largest digit in the number

# num = int(input())
# max = 0
# while num != 0:
#     r = (num % 10)
#     if r > max:
#         max = r
#     num = num //10
# print(max)



# given a list of numbers create a result list having len as 3 where 1st elements is the sum of prime numbers present, 
# second element is the no of prime numbers and third element is the no of composite numbers

# sum_prime = 0
# count_prime = 0
# count_comp = 0

# for i in [34, 79, 61, 1, 56, 99, 23, 7, 49]:
#     for j in range(2, i):
#         if i % j == 0:
#             count_comp +=1
#             break
#     else:
#         sum_prime += i
#         count_prime += i
# print(sum_prime)
# print(count_prime)
# print(count_comp)

# using functions
'''
l = [34, 79, 61, 1, 56, 99, 23, 7, 49]
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(4))

sum_prime = 0
count_prime = 0
count_comp = 0
for i in l:
    if is_prime(l):
        sum_prime +=1
        count_prime +=1
    else:
        if i != 1:
            count_comp += 1

res = [sum_prime, count_prime, count_comp]
print(res)
'''

'''
A company gives performance points to employees.
The HR manager wants to identify all employee pairs where one employee’s score is exactly double the other employee’s score.
Write a Python program to find all such pairs from the list.

Input:
scores = [2, 4, 6, 8, 3, 12]Output:
[(2, 4), (4, 8), (6, 12), (3, 6)]
Because:
4 = 2 × 2
8 = 4 × 2
12 = 6 × 2
6 = 3 × 2
'''

# scores = [2, 4, 6, 8, 3, 12]
# for i in range(len(scores)):
#     for j in range(i + 1, len(scores)):
#         if scores[i] == 2*scores[j]:
#             res.append(scores[i], scores[j])
#         elif scores[j] == 2*scores[i]

'''
A company stores product codes as strings.
Sometimes the same code is entered in rotated form.
Example:
"ABCD" rotated becomes "BCDA"
"ABCD" rotated becomes "CDAB"
The manager wants to find all pairs of strings where one string is a rotation of another.
Write a Python program to find all such pairs.



Input:
codes = ["ABCD", "BCDA", "XYZ", "YZX", "HELLO", "WORLD"]Output:
[('ABCD', 'BCDA'), ('XYZ', 'YZX')]

What is Rotation?
If one string can be shifted circularly to form another.
Example:
ABCD -> BCDA -> CDAB -> DABC
All are rotations of "ABCD".
'''


# codes = ["ABCD", "BCDA", "XYZ", "YZX", "HELLO", "WORLD"]
# res = []
# for i in range(len(codes)):
#     st = 2*codes[i]
#     for j in range(i + 1, len(codes)):
#         if codes[j] in st:
#             pair=[codes[i], codes[j]]
#             res.append(pair)
# print(res)


# WAP TO PERFORM CLOCK WISE KTH ROTATION
'''
A store records its daily profit/loss amounts in a list of integers.
Positive numbers = profit
Negative numbers = loss
Zero = no change
The manager wants to know if there exists any continuous sequence of days (subarray) whose total profit/loss is exactly equal to a given target amount.Task:
Write a Python program to check whether the list contains any subarray whose sum is equal to the target value.

Input:
sales = [3, 4, -2, 5, 1, -3]
target = 7Output:
TrueExplanation:
The continuous subarray:
[3, 4]
has sum:
3 + 4 = 7
So the answer is True.
'''

# sales = list(input())
# target = int(input())
# for i in range(len(sales)):
#     for j in range(i + 1, len(sales)):
#         if sales [i] + sales[j] == target:
#             print(True)
# print(False)



# find the largest repeating substring


# s = 'banana'
# longest = ''
# for i in range(len(s)):
#     for j in range(i+1, len(s)+1):
#         sub = s[i:j]
#         # print(sub)
#         count = 0
#         for k in range(len(s)- len(sub)+1):
#             if s[k:k+len(sub)]==sub:
#                 count+=1
#         if count > 1:
#             if len(sub)>len(longest):
#                 longest = sub
# print(longest)



