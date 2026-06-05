


#-------- GLOBAL VARIABLE
'''
--> IT IS A TYPE OF VARIABLE WHICH WILL PRESENT OUTSIDE THE FUNCTION MEANS INSIDE THE MAIN SPACE

--> 
'''
a = 10
def greeting():
    global a
    a = 20 # it got created inside the method area
    print('a:', a)
    print("good morning")
greeting()
print(a)