# string = 'PYTHON@123'
# print(string.lower())



# string = 'python@123'
# print(string.upper())


# --------- TITLE 
# CHANGE THE FIRST LETTER IN EVERY WORD TO CAPITAL AND REMAINING TO SMALL LETTERS

# s = 'i love python programming'
# print(s.title())




#---- CAPITALIZE 

# IN BUILT FUNCTION USED TO 
# SYNTAX : var_name.capitalize() or, string.capitalize() 
# it is used to convert the starting alphabet of a string into uppercase and the remaining into lowercase

# s = 'python'
# print(s.capitalize())

# print('PROGRAMMING LANGUAGE'.capitalize())


# ------------ ISLOWER()

# SYNTAX: var_name.islower() or, string.islower()
# it is used to check wether the alphabets are in lowercase or not. if the string doesn't consist of alphabets it will return the output as FALSE

# s = 'pytHon'
# print(s.islower())
# print('python@123'.islower())




#--------- ISUPPER()
#SYNTAX: var_name.isupper() OR, string.isupper()
# # it is used to check wether the alphabets are in uppercase or not. if the string doesn't consist of alphabets it will return the output as FALSE

# s = 'PYTHON'
# print(s.isupper())
# print('PYTHON@123'.isupper())
# print()



#---------------isalpha()
# SYNTAX : var_name.isalpha() or, string.isalpha()
# it is used to check whether rhe string consists of only alphabets or not

# print('python'.isalpha())
# print('python@123'.isalpha())
# print('PYtHoN'.isalpha())


#----------alnum()
#SYNTAX : var_name.isalnum()
#it is used to check whether the string consists of alphabets or digits or both alphe-numeric or not
# print('python123'.isalnum())
# print('python@123'.isalnum())


#--------------- isdigit()
# SYNTAX: var_name.isdigit()  or, string.is_digit()
# it is used to check wether the string consists of only digits or not
# print('py@123'.isdigit())
# print('123'.isdigit())



#------------isspace()




#------------index()
# SYNTAX : var_num.index(substr) or, string.index(substr)
#it is used to return the index value 






#-------FIND()



#-----COPY()
#syntax dest_var = source_var.copy()
#it is used to perform shallow copy
# 
# source_var = [1, 2, 3]
# dest_var = source_var.copy()
# print('source_var', id(source_var))
# print('destination_var:', id(dest_var)) 



#-----------COUNT()
#syntax : var_name.count(val)
# it is used to check how many time a particular value got repeated inside the existing list collection
# list_coll = [1, 2, 3, 2, 2, 1]
# print('1:', list_coll.count(1))
# print('2:', list_coll.count(2))
# print('3:', list_coll.count(3))
# print('10:', list_coll.count(10))


# tpl_coll = (1, 2, 3, 4, 1, 2)
# print('1:', tpl_coll.count(1))
# print('2:', tpl_coll.count(2))
# print('3:', tpl_coll.count(3))
# print('10:', tpl_coll.count(10))


# --------INDEX()
#SYNTAX : var_name.index(val)
# it is used to retreve the index number for the given value if the value is not there, it throw error

# list_coll = [1,2,3, 2,2,1]
# print(list_coll.index(1))
# print(list_coll.index(3))
# # print(list_coll.index(10))


# tpl_coll = (1, 2, 3, 4, 1, 2)
# print(tpl_coll.index(1))
# print(tpl_coll.index(3))



# --------- SORT()
# syntax : var_name.sort(reverse=False)
# IT IS USED TO ARRANGE THE LIST VALUES EITHER IN ASCENDING OR DESCENDING ORDER 
# coll = [5,2,1,4,2]
# # SORTING IN ASCENDING ORDER
# coll.sort()
# print(coll)

coll = [5,2,1,4,2]
# SORTING IN deSCENDING ORDER
# coll.sort(reverse=True)
# print(coll)



# ---------- REVERSE()
#SYNTAX : var_name.reverse()
# it is used to reverse the position of a list collection
# coll = [5, 2, 1, 4, 3] # it will never sort it will reverse the list 
# coll.reverse()
# print(coll)



#------- ADD()
#SYNTAX : var_name.add(value)
# it is used to add a new inside an existing set collection
# set_coll = {1, 2, 3}
# set_coll.add('hi')
# print(set_coll)


# --------- CLEAR()
# SYNTAX : var_name.clear()
# it is used to remove all the existing value from the set collection and make the set empty
# set_coll = {1, 2, 3, 4, 5}
# set_coll.clear()
# print(set_coll)


# -------- copy()
# syntax : dest_var = source_var.copy()
# it is used to perform shallow copy operation



# ---------- REMOVE()
#SYNTAX : var_name.remove(value)
# it is used to remove a particular value form an existing set collection, if the value will not present it will through error 
# set = {1, 2, 3, 4, 5}
# set.remove(2)
# set.remove(20)#error
# print(set)



# ----- DISCARD()
#SYNTAX : set_coll.discard(value)
# it is used to remove a particular value from an existing set collection, 
# if the value is present then it will remove, other wise it will not throw error
# set_coll = {1, 2, 3, 4, 5}
# set_coll.discard(2)
# print(set_coll)


# ----------- UPDATE()
# SYNTAX : var_name.update(value)
# it is used to add multiple values inside an existing set collection in the form od iterable

# set_coll= {1, 2, 3, 4, 5}
# set_coll.update([10, 20, 30])
# print(set_coll)



#------- pop()
# syntax : var_name.pop()
# it is used to remove a random value from an existing set collection at a time it remove a single value



# ------- UNION()
# SYNTAX : set_1.union(set_2, ...., set_n)
# it is used to return a new set collection consists of the values of all other set collections

# set_1 = {1, 2, 3, 4, 5}
# set_2 = {3, 4, 5, 6, 6}
# new_set = set_1.union(set_2, {10, 20, 30}, {11, 12, 13})
# print(new_set)


# ------ DIFFERENCE()
# SYNTAX : SET_1.DIFFERENCE(SET_2)
# IT IS USED TO RETURN A NEW SET COLLECTION CONSISTS OF THE UNIQUE VALUES OF THE FIRST SET

# set_1 = {1, 2, 3, 4, 5}
# set_2 = {3, 4, 5, 6, 7}
# print('set_1: ', set_1.difference(set_2))
# print('set_2: ', set_2.difference(set_2))


#-------SYMMETRIC_DIFFERENCE()
#SYNTAX : set_!.symmetric_difference(set_2)
# it is used to return a new set collection consists if unique values from both the set collection

# set_1 = {1, 2, 3, 4, 5}
# set_2 = {3, 4, 5, 6, 7}
# print(set_1.symmetric_difference(set_2))


# -------- INTERSECTION()
#SYNTAX : set_1.intersection(set_2, .... , set_n)
# it is used to return a new set collection consists if the common values present between all the sets

# set_1 = {1,2, 3, 4, 5}
# set_2 = {3, 4, 5, 6, 7}
# print(set_1.intersection(set_2))




# --------ISSUBSET()
# -------- ISSUPERSET()

# superset = {1, 2, 3, 4, 5}
# subset = {1, 2, 3}
# print(subset.issubset(superset))
# print(superset.issuperset(subset))


# ----- GET()
#SYNTAX : var_name.get(key)
# it is used to return the value of an existing key present inside the dictionary if the key name is not present then it will return none

# user = {
#     "username": "user123",
#     "password": "1234",
#     "is_logged_in": True,
# }
# print("username:",user.get("username"))
# print("password:", user.get("password"))
# print("login.devices:", user.get("login_devices"))


# ------- UPDATE()
#SYNTAX: var_name.update((key1:val1, key2:val2, ....., keyn:valn))
#it is used to add multiple key value pairs inside an existing dictionary

# user = {
#     "username": "user123",
#     "password": "1234",
#     "is_logged_in": True,
# }
# extra_info = {"login_devices": ["windows", "linux"], "recent_login_time": "10:33 AM"}

# user.update(extra_info)
# print(user)

