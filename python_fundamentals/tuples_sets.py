'''
#Tuples: 
- ordered collection
- immutable, cannot delete or update
- they are faster than lists 
- it makes your code safer
- valid keys in dictionary
- can have duplicate value
'''

numbers = (1,2,3,4)
alphabet = ("a","b","c","d")
numbers[1] #to access

my_list = [1, 2, 3, "Python"]
new_tuple = tuple(my_list) #create new tuple

#tuples as keys
locations = {(2342.23,2342.34): "USA", (13413.22,1341.11):"Nepal", (14535.44,34564.34):"UK"}
print(f"keys: {locations.keys()}")
print(f"USA: {locations[(2342.23,2342.34)]}")

#Tuple methods:
#count() - returns the number of times value appers in tuple
numbers.count(1)

#index() - returns the index at which a value is found in tuple
numbers.index(1)

'''
Sets:
 - they do not have duplicate values/unique
 - they are not ordered 
 - cannot access items by index since no order 
'''

s = set({1,2,3,4,4,5}) #1,2,3,4
new_set = {5,7,8}

5 in new_set #True

#Sets Methods
#add(x) - add element to the set. if element already preset, set doesnt change
s.add(6) #1,2,3,4,6
s.add(6) #1,2,3,4,6

#remove(x) - remove the value from the set
s.remove(6) #1,2,3,4
s.remove(6) #keyError
s.discard(6) #doesnt do anything

#copy() - makes the copy of the set
copy_set  = s.copy()

#clear() - remove the entire content of the set 
copy_set.clear()

#set union
set1 = {1,2,3,4}
set2 = {3,4,5,6}
set1 | set2 #returns union set
set1 & set2 #returns common in both sets 

#set comprehension
set_new = {x**2 for x in range(10)} #this is set
what_is_this = {x:x**2 for x in range(10)} #this is dictionary

duplicate = {char.upper() for char in 'hello'} #{H,E,L,O}

{char for char in 'hello' if char in 'aeiou'} #{e,o}













