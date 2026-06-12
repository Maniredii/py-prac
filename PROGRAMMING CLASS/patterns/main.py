'''
right angle triangle (increasing)

description : stars increase by one per row, left aligned

*
* *
* * *
* * * *
* * * * *

rows | star | space
 1      1       0
 2      2       0
 3      3       0
 4      4       0
 5      5       0
'''
# n = int(input("Enter rows : "))
# for i in range(1, n+1):
#     print("* " * i)


'''
left aligned triangle 

    *
   **
  ***
 ****
*****
rows(n) | star | space
 1         1       4
 2         2       3
 3         3       2
 4         4       1
 5         5       0

'''
# n = int(input("Enter rows : "))
# for i in range(1, n+1):
#     # for j in range():
#         print(" "*(n-i), end = '')
#         print("*"*i)


# n = int(input("Enter rows : "))
# for i in range(1, n+1):
#     # star = i
#     # space = n-i
#     print(" "* (n - i) + '*' * i)

'''
* * * * *
* * * *
* * *
* *
*
rows(n) | star | space
 1         5       0
 2         4       0
 3         3       0
 4         2       0
 5         1       0

'''

# n = int(input("Enter no.of rows : "))
# for i in range(n, 0, -1):
#     print("* "*i)

'''
* * * * *
  * * * *
    * * *
      * *
        *
rows(n) | star | space
 1         5       0
 2         4       1
 3         3       2
 4         2       3
 5         1       4
'''
# n = int(input("Enter no.of rows : "))
# for i in range(1, n+1): 
#     star = n-i + 1 
#     space = i -1
#     print(" "*space + "*"*star)

'''

   *
  *** 
 ***** 
*******

'''
# n = int(input("Enter no.of rows: "))
# for i in range(1, n+1):
#     space = n - i
#     star = 2*i - 1
#     print(" "*space + "*"*star) # another print approach-- print(" "*(n-i) + "*"*(2*i-1))


'''
*******
 ***** 
  *** 
   *

'''

# n = int(input("Enter no.of rows : "))
# for i in range(n, 0, -1):
#     # space = n - i
#     # star = 2*i - 1
#     print(" "*(n-i) + "*"*(2*i - 1))


'''
    *
   *** 
  ***** 
 *******
*********
 *******
  ***** 
   *** 
    *
'''

# n = int(input("Enter no.of rows : "))
# for i in range(1, n+1):
#     print(" "*(n - i)+ "*"*(2*i -1))
# for j in range(n-1, 0, -1):
#     print(" "*(n - j)+"*"*(2*j-1))


'''

    *
   * * 
  *   * 
 *     *
*       *
 *     *
  *   * 
   * * 
    *

rows | star | innerspace | outerspace
 1      1          0            4
 2      2          1            3
 3      2          3            2
 4      2          5            1
 5      2          7            0

'''
# n = int(input("Enter no.of rows : "))
# for i in range(1, n+1):
#     inner = 2*i-3
#     outer = n - i
#     if i == 1:
#         print(" "*outer+"*")
#     else:
#         print(" "*outer+"*"+" "*inner+"*")
# for i in range(n-1, 0 , -1):
#     inner = 2*i-3
#     outer = n - i
#     if i == 1:
#         print(" "*outer+"*")
#     else:
#         print(" "*outer+"*"+" "*inner+"*")


'''
*******
 ***** 
  *** 
   *
   *
  *** 
 ***** 
*******
'''

# n = int(input("Enter no.of rows : "))
# for i in range(n, 0 ,-1):
#     print(" "*(n-i)+"*"*(2*i-1))
# for i in range(2, n+1):
#     print(" "*(n-i)+"*"*(2*i-1))



'''
*
**
***
****
*****
****
***
**
*
'''

# n = int(input("Enter no.of rows : "))
# for i in range(1, n+1):
#     print("*"*i)
# for i in range(n-1, 0, -1):
#     print("*"*i)

'''
*
**
* *
*  *
*****

rows | star | inner space(i-2)
  1     1           0
  2     2           0
  3     3           1
  4     2           2
  5     5           0

'''

# n = int(input("enter no.of rows : "))
# for i in range(1, n+1):
#     if i ==1 or i == n:
#         print("*"*i)
#     else:
#         space = i - 2
#         print('*' + ' ' * space + '*')


'''

*****
*  *
* *
**
*

'''

# n = int(input("enter no.of rows : "))
# for i in range(n, 0, -1):
#     if i ==1 or i == n:
#         print("*"*i)
#     else:
#         space = i - 2
#         print('*' + ' ' * space + '*')


'''
   *
   * *
  *  *
 *    *
********
'''

# n = int(input("Enter no.of rows : "))
# for i in  range(1, n+1):
#     # inner = 2*i-3
#     # outer = n - i
#     if i == 1:
#         print(' '* (n-i) + '*')
#     elif i == n:
#         print(' '*(n - 1)+'*'*(2*i-1))
#     else:
#         print(' '*(n-i)+'*'+' '*(2*i-1)+'*')


'''
*****
*   *
*   *
*   *
*   *
*****

'''

# n = int(input("Enter no.of rows : "))
# for i in range(1, n+1):
#     if i == 1 or i == n:
#         print('*'*n)
#     else:
#         print("*" + ' '*(n-2)+'*')


'''
* * * * *
* *   * *
*   *   *
* *   * *
* * * * *

'''

# n = int(input("Enter no.of rows : "))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == j or i+j == n+1 or i == 1 or j == 1 or j == n or i == n:
#             print('*', end = ' ')
#         else:
#             print(' ', end=' ')
#     print()


'''
  *
  *
*****
  *
  *
'''
n = int(input("Enter no.of rows : "))
for i in range(1, n+1):
    mid = n//2
    if i == mid+1:
        print('*'*n)
    else:
        print(' '*mid+"*")

    