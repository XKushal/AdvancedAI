#Example 1
#Write a function called product that accepts two parameters and returns the product of the two parameters
def product(a,b):
	return a * b

print(product(2,-2))

#Example 2
#returns the day of the week, takes one parameter as number of day(1-7)
def return_day(number):
    days = {
        1:"Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    return days.pop(number) if number in days.keys() else None
print(return_day(5))

#Example 3
#function returns the number of times that letter appears in the word
def single_letter_count(str1, str2):
    return tuple(str1.upper()).count(str2.upper())
    
print(single_letter_count("Hello World", "h"))

#Example 4
#returns a dictionary with the keys being the letters and the values being the count of the letter.
def multiple_letter_count(str1):
    return {letter:str1.count(letter) for letter in str1}

print(multiple_letter_count("awesome"))

#Example 5
#list manipulation
def list_manipulation(list1, command, location, value=None):
    if command == "remove" and location == "end":
        return list1.pop()
    elif command == "remove" and location == "beginning":
        return list1.pop(0)
    elif command == "add" and location == "beginning":
        list1.insert(0, value)
        return list1
    else:
        list1.append(value)
        return list1
        
print(list_manipulation([1,2,3], "add", "beginning", 20))

#Example 6
#palindrome
def is_palindrome(word):
    word = word.replace(" ","").upper()
    reverse_word = word[-1::-1]
    
    if word == reverse_word:
        return True
    return False
    
print(is_palindrome('my name issi eman y m'))

#Example 7: Frequency
def frequency(list1, search_term):
    return list1.count(search_term)
    
print(frequency([True, False, True, True], False))

#Example 8: multiply_even_numbers
def multiply_even_numbers(list1):
    total = 1
    if list1:
        for num in list1:
            if num % 2 == 0:
                total = total * num
    return total
    
print(multiply_even_numbers([]))

#Example 9: capitalize first letter 
def capitalize(str1):
    return str1[0].upper() + str1[1:]

print(capitalize("matt"))

#Example 10: returns truthy values
#option 1 
def compact(list1):
    truthy = []
    for x in list1:
        if x:
            truthy.append(x)
    return truthy

#option 2:
def compact(list1):
	return [value for value in list1 if value]

print(compact([0,1,2,"",[], False, {}, None, "All done"]))

#Example 11: returns common values from two lists
#option 1
def intersection(list1, list2):
    return list(set(list1) & set(list2))

#option 2:
def intersection(l1, l2):
    return [val for val in l1 if val in l2]
    
print(intersection(['a','b','z'], ['x','y','z']))

#Example 12: callback function
def isEven(num):
    return num % 2 == 0

#option 1:
def partition(list1, callback_function):
    truthy_list = []
    falsly_list = []
    for x in list1:
        if callback_function(x):
            truthy_list.append(x)
        else:
            falsly_list.append(x)
    return [truthy_list, falsly_list]

#option 2:
def partition(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]
    
print(partition([1,2,3,4], isEven))

#Example 13: *args operator: contains all passed arguments in tuple
#all = anything after actual params and before deault parameters and **kwargs
def contains_purple(*args):
    for arg in args:
        if arg == "purple":
            return True
    return False

#option 2:
def contains_purple(*args):
    if "purple" in args: return True
    return False

print(contains_purple("green", False, 37, "blue", "hello world"))


#Example 14: **kwargs (keyword arguments):  gather remaining arguments and store in dictionary 

def combine_words(word, **kwargs):
    if "prefix" in kwargs:
        return kwargs["prefix"] + word
    elif "suffix" in kwargs:
        return word + kwargs["suffix"]
    else:
        return word
print(combine_words("child"))
print(combine_words("child", prefix="man"))
print(combine_words("child", suffix="ish"))

def math(**kwargs):
	return kwargs["operation"](kwargs["first"])

print(f"kwargs operation: {math(operation=isEven, first=10)}")

#Example 15:
#option 1:
def add(first, second):
    return first + second

def subtract(first, second):
    return first - second

def multiply(first, second):
    return first * second

def divide(first, second):
    return first / second

def calculate(**kwargs):
    operation_result = kwargs["operation"](kwargs["first"], kwargs["second"])
    operation_result = float(operation_result) if kwargs["make_float"] else int(operation_result)
    if "message" in kwargs:
        return f'{kwargs["message"]} {operation_result}'
    else:
        return f'The result is {operation_result}'
    
print(calculate(make_float=False, operation=add, message='You just added', first=2, second=4) )
print(calculate(make_float=True, operation=divide, first=3.5, second=5) )
















