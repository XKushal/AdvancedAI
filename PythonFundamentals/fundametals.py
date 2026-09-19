print("Hello World")
print("Becoming an AI Engineer")
print()

#Numbers and Math
#ints, floats, operators (**, %, //)

print("Variabls and DataTypes")
x = 100
y = 2
print(f"sum of {x} and {y}  is : {x + y}")
print()

# Naming restrictions: 
 # - must start with the letter or underscore 
 # - names are case-sensitive


# Naming conventions:
#  - variabls should be snake_case
#  - most variabls should be lowercase with some exceptions (like constants, or UpperCamelCase for class)
#  - variables that start and end with two underscores called "dunder" are supposed to be private or left alone
#  	__dont_touch__

#Data Types - for eg: bool, int, str, list, dict
#Dynamic typing: highly flexible about reassigning variables to different types

#Strings: declaring strings try to make it consistent either double or single quotes
#String Escape Characters : \n, \\, \" etc
#String Concatenstion

print("Formatting Strings - using F-strings")
first_name = "Kushal"
last_name = "Singh"
name = f"fstring  - First Name: {first_name}, Last Name: {last_name}"
name_two = "with format - First Name: {}, Last Name: {}".format(first_name, last_name)
print(name)
print(name_two)
print()

#Converting Data Types: int(variable), str(my_list), float(variable)

#input
print("user input")
print("how many miles did you run today?")
kms = input()
miles = float(kms)/1.60934
miles = round(miles, 2)
print(f"Ok, you ran {miles} miles")
print()

#Conditional Statements
print("Conditional Statements")
number = input("Enter a number: ")
number = int(number)
if number < 10:
	print("Number is less than 10")
elif number > 10 & number < 100:
	print("Number is greater than 10 and less than 1000")
else:
	print("Number is greater than 100")

#Logical Operators: and, or, not
#is: checks for the memory, ==: checks for the value
#LOOPS - for and while, keyword: break
print()
print("LOOPS - for and while, keyword: break;")
x = input("how many times you want to print? ")
for i in range(0,int(x)):
	print(f"Print: {i}")

#LISTS
print()
print("LISTS: collection or group of items\n")
#lists(range(1,5)) - creates a list 
#[] - this is also a list
# append(x) - add only one item x to the end of the list
# extend() - add multiple items to the list
# insert(index, item) - insert item to the list at "index"

# clear() - remove all the items in the list (list becomes empty)
# pop() - remove/returns last item by default
# pop(index) - remove/returns the item at "index"
# remove(value) - remove the actual "value" from the list. if duplicate removes 1st

# index(item) - returns the index of an item from the list
# index(item, starting_index) - returns the index of an item from list but start with starting_index
# index(item, starting_index, ending_index) - returns the index of an item from list within the given range of indexes 

# reverse() - reverse the items in the list
# sort() - sorts the items in ascending order in list
# join() - convert lists into strings. for eg, " - ".join(this_is_list)

#slicing - (:) - make new list using slices of the old list. old_list[start_index:end_index:step]
#swap values with comma a[1],a[2] = a[2],a[1]

#List comprehension with conditional logic
print("List comprehension with conditional logic")
print("Make the initial letter Capital.")
names  = ["kushal", "singh", "nepal"]
uppercase_names = [(name[0].upper() + name[1:]) for name in names]

nums = [1,2,3,4,5,6,7,8,9]
evens = [num for num in nums if num % 2 == 0 ]
odds = [num for num in nums if num % 2 != 0]

[num/2 if num % 2 == 0 else num * 2 for num in nums]


print("\nNested List comprehension with conditional logic")
nested_lists = [[1,2,3],[4,5,6],[7,8,9]]
board = [[num for num in range(1,4)] for val in range(1,4)]
[["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)]

#Dictionary
# dict.keys() - access keys in the dictionary
# dict.values() - access values in the dictionary 
# dict.items() - access both keys and values in the dictionary

# clear() - clear the dictionary
# copy() - makes the clone of the dictionary
# fromkeys([],value) - creates key-value pairs from comma separated (this is tricky with list or string)
# get(key) - get the value of the give key

scores = {"A": 10, "B": 20, "C": 30, "D": 40, "E": 50}
for i, j in scores.items():
	print(i, j)

# pop(key) - pop/remove the value of the key from the dictionary
# popitem() - remove random from the dictionary (need to check order)
# update() - update k,v in a dictionary with another set of k,v
s = dict(F=60, E=70)
scores.update(s)






































































































