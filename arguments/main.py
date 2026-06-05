

# --------- keyword argument

'''
def addTwoNums(n1, n2):
    print('N1:', n1)
    print('N2:', n2)
    print(n1 + n2)
addTwoNums(n2 = 20, n1 = 5)

'''


# ------ VARIABLE LENGTH ARGUMENT
def temp(*args, **kwargs):
    print(args)
    print(kwargs)
temp(1, 2, 3, {10, 20}, {'a':1, 'b':2}, fullname='PFD', siblings = ['anaconda', 'miniconda'])

