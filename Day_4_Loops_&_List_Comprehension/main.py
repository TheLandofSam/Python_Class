'''
Log quote in Python is 3 single quotes to open and close

A function (fx) is a re-useable block of code that performs a specific task.

List Comprehension is a shorter and more readable way to create lists.

Key Difference:
- Parameter (Param) -> The variable inside the fx def that acts as a placeholder.
- Argument -> The actual value passed when calling the fx.

'''
# functions (fxs) and list comprehension
# need fxs keep you from re-writing the same logic, makes it easier to repeat code
# Syntax of a function: def. Then give the fx a name. In the parenth add parameters.
# 'name: str = Sam' is how you state the type of a variable

def function_name(parameters):
    #code block, loops, whatever, anything
    return #not always necessary if you are just doing simiple thing like a print

#Basic fx, without parameters

def greet():
    print('Hello class!!')

# to call fx, name plus open parenth

greet() # calling fx

#fx can be called anywhere you want it
#Function with params


def greet_user(name):  #name is out param (variable)
    print(f'Hello {name}')

greet_user('Sam')

#Fx that retun a value

def add_num(a, b):
    return a + b

sum = add_num(3, 13)
print(sum)

# fx user

def user(name, age, city = ''): # can send in empty value and still create param this way user(name, age, city = '') or typing 'None' instead of open quites
    # key word pass, I've created it, but for now just skip it now, I am not going to do anything with it now, but I can go back later and finish it
    if name == 'Sam' and age == 49:
        print(f'Hello Sam')
    elif name == 'Feliciti' and age == 31:
        print ('Hello Feliciti')

    if city == 'Boise':
        print('Welcome to the class!!)')

# Sending values (arguments) without city
user('Sam', 49)

# sending all values (arguements)
user('Sam', 49, 'Boise')

#List Comprehension

numbers = [1,2,3,4,5] # list of numbers
squared_numbers = [] # empty list
for num in numbers:
    squared_numbers.append(num ** 2) # create new list of squared numbers
print(squared_numbers)

#syntax list comprehension

#new_list = [expression for item in collection if condition]

#Creating a list with List Comprehension

numbers = [1, 2, 3, 4, 5]
squared_numbers = [num*2 for num in numbers]

print(squared_numbers)
