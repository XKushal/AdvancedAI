#example1
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

#output: {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}

answer = {}
answer_2 = {}

# option1
for state in list1:
	value = list2.pop(0)
	answer[state] = value

#option 2
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
answer_2 = {list1[i]:list2[i] for i in range(0,3)}

#option3
dict(zip(list1,list2)) 

print(f"option1: {answer}")
print(f"option2: {answer_2}")

#example2

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
#output: {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}

#option1:
person_dict = {i:j for i,j in person}

#option2:
dict(person)

print(f"person_dict: {person_dict}")

#example 3
#output: {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

#option1
keys = ["a","e","i","o","u"]
vowel = {keys[i]:0 for i in range(0,5)}
print(f"vowel: {vowel}")

#option2
letters = "aeiou"
option2 = dict.fromkeys(letters, 0)
print(f"option2 vowel: {option2}")

#example 4
#create dictionary that maps ASCII keys to their corresponding letters

ascii_values = {i:chr(i) for i in range(65,91)}




