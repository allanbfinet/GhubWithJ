print("good morning")  #print -> display values 
print(45+34)   #arithmetic operators 

greeting = "good morning"
print(greeting)

# data type 
print(type(greeting))   #string


    # ARITHMETIC OPERATORS 
# Addition  
addition = 45 + 34
print(type(addition))   # integer

value = True 
print(type(value))

# subtraction 
substraction =  45 - 34
print(type(substraction))   # integer

print(substraction)

# multiplication 
multiplication  = 4 * 3
print(type(multiplication)) # integer

print(multiplication)

# division  
division = 45 / 34
print(division)

# modulus  -> uses % 
        #  -> displays the remainder
# variablename       value 
modulus       =     45 % 34
print(modulus) 


# PYTHON DATA TYPES  
# A. Primitive data types 
        # -> have single values
# B. Non-primitive data types 
        # -> has multiple values 



# A. Primitive data types 
        # -> are fundamental or foundational in python 
        # -> have single values
# Examples; 
#string; 
message = "Hello World!"
#integer 
x = 10
#boolen 
Is_valid = True or false  
#float
y = 3.24 


# B. Non-primitive data types 
        # -> are more complex data structures and built using primitive data types.
        # -> have multiple values
# 1. List 
    # -> ordered collection of items
numbers = [1, 2, 3, 4, 5]

# accessing values off of a list 
    # A. indexing a list 
print(numbers[0]) # to print the first item (1)
print(numbers[-1]) # to access the last number on the list why [-1]?
    # B. Slicing a list 
# write your code here  



# reassignment in a list 
numbers[3] = 10 # Change the fourth item (index 3) to 10
print(numbers) # Output: [1, 2, 3, 10, 5]

# methods in a list 

#  -> .append()
# Adds an item to the end of the list
numbers.append(6)
print(numbers) # Output: [1, 2, 3, 10, 5, 6]

#  -> .insert()
# Inserts an item at a specific position
numbers.insert(1, 55)
print(numbers) # Output: [1, 55, 2, 3, 10, 5, 6]

#  -> .remove()
# Removes the first occurence of the item
numbers.remove(10)
print(numbers) # utput: [1, 55, 2, 3, 5, 6]

# NESTED LIST  
    # ->  accessing values off of a nested list
    # A list inside another list

matrix = [
    [1, 2, 3], # row 0
    [4, 5, 6], # row 1
    [7, 8, 9] # row 2
]

# Accessing values from a nested list:

print(matrix[0][0]) # first row
print(matrix[1][2]) # second row
print(matrix[2][1]) # third row

# 2. Tuple 
coordinates = (3, 4)

# understand the difference btn tuple and list  

# -> Tuple uses ( ) | List uses [ ]
# -> Tuple is immutable (Cannot change its values)
# -> List is mutable (Can change its values)

# accessing values off of a tuple  
#   -> indexing in a tuple 

print(coordinates[0]) # Output: 3
print(coordinates[1]) # Output: 4

#   -> slicing in a tuple 

print(coordinates[0:2]) #
print(coordinates[:1])
print(coordinates[1:]) 

# tuple unpacking 

x, y = coordinates
print(x) 
print(y)

# 3. Dictionary
    # -> collection of key value pairs
person = {
    'name': 'John',
    'age': 30, 
    'city': 'New York'
}

# accessing values in a dictionary  
print(person['name'])
print(person.get('age'))

# modifying a dictionary   
# -> adding new values 
person['email'] = 'john@person.com'
print(person)
# -> add new key and values 

# reassignment in a dictionary  
person['age'] = 31
print(person)

# methods in  a dictionary  
# -> .keys() 
print(person.keys())
# -> .values() 
print(person.values())
# -> .items() 
print(person.items())

# NESTED DICTIONARY  
    # ->  A dictionary inside another dictionary

student = {
    'name': 'Diane',
    'grades': {
        'math': 90,
        'history': 85
    },
    'address': {
        'city': 'Boston',
        'ZipCode': '02118'
    }
}

# ->  accessing values off of a nested dictionary

print(student['grades']['math']) # Output: 90
print(student['address']['city']) # Output: Boston
# 4. Set
   # -> Unordered collection of unique items
unique_numbers = {1, 2, 3, 4, 5}

# accessing values in a set  

# methods in a set  
#  -> .add()





# COMPARISON OPERATOR 
# -> examples 
#          >, <, ==



    # COMBINING COMPARISON OPERATOR  & LOGICAL OPERATOR





# BRANCHING IN PYTHON  
# IF-ELSE-ELIF STATEMENTS  

# IF STATEMENT  
# if condition:       condition -> bool
#     statement1 
#     statement2  

if 3 == 2:     # evaluated to False
    print('2 is equal to 2')


# IF-ELSE STATEMENT 
if 3 == 2:     # evaluated to False
    print('3 is equal to 2')
# if 34 > 20:
#     print('34 is greater than 20')
else: 
    print('3 is not equal to 2')


print('\n IF-ELIF-ELSE')  # newline to separate codes
# IF-ELIF-ELSE  
if 3 == 2:     # evaluated to False
    print('3 is equal to 2')
elif 34 > 20:
    print('34 is greater than 20')
elif 100 == 100: 
    print('100 is equal to 100')
elif 90 < 100: 
    print('90 is LESS THAN 100')
else: 
    print('3 is not equal to 2')


#  NESTED IF STATEMENTS  
# if condition:
#     statement1  
#     if condition: 
#         statement1a

print('\n NESTED IF STATEMENT')
if 23 == 24:  #false
    print('23 is equal to 24')
    if 20 > 10:    # Child if statements
        print('20 is greater than 10')
    else: 
        print('20 is not greater than 10')
else: 
    print('23 is NOT EQUAL to 24')
    if 10 > 9: 
        print('10 is greater than 9')
        if 10 % 2 == 0: 
            print("10 is divisible by 2")
        else: 
            print("10 is NOT divisible by 2")



print('\n LOOPS IN PYTHON')
# LOOPS IN PYTHON  
# -> iterate through items/sequences 

# For loop 
# -> allow you to iterate through a sequence   
numbers = [1, 2, 3, 4, 5]     # list -> uses square brackets

for i in numbers: 
    print(i)


new_list = []   # create an empty list 
for i in numbers: 
    print("squaring", i, "to: ", i**2)
    new_list.append(i**2)     # .append() method in a list

print("our new list is: ", new_list)
print('the final value i: ', i)


# looping through a dictionary 
person = {'name': 'John', 'age': 30, 'city': 'New York'}

for i in person.values():  # use of .values() method
    print(i)


for key, value in person.items(): 
    print("the key is: ", key, " and the value is: ", value)




# while loop 
# -> continually perform an action until some condition is met. 


# IF STATEMENT  
# if condition:       condition -> bool
#     statement1 
#     statement2 

# while condition: 
    # statement1 
    # statement2 


num = 2 

while num < 5:     # num- integer dtype
    print(f"number is: {num}")
          # f-string (formatted string)
    num = num + 1 

# [TASK] break & continue in loops 