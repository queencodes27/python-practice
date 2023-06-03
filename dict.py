"""
Exercise 1: Convert 
two lists into a dictionary
"""
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# mydict = {}
# for i in range(len(keys)):
#     mydict[keys[i]] = values[i]
# print(mydict)

"""
Exercise 3: Print the 
value of key ‘history’ from the below dict

"""
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }

# print(sampleDict['class']['student']['marks']['history'])

"""
Exercise 4: Initialize dictionary 
with default values

"""
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# init = dict.fromkeys(employees, defaults)
# print(init)
"""
Exercise 5: Create a dictionary by 
extracting the keys from a given dictionary
"""
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # Keys to extract
# dict = {}
# keys = ["name", "salary"]
# for i in keys:
#     dict[i] = sample_dict[i]
# print(dict)
"""
Exercise 6: Delete a list of keys from a dictionary
"""

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# # Keys to remove
# keys = ["name", "salary"]
# for i in keys:
#     sample_dict.pop(i)
# print(sample_dict)
    
    





"""
Exercise 7: Check if 200 value exists in a dictionary
"""
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# values = sample_dict.values()
# if 200 in sample_dict.values():
#     print("yes 200 exists")
# else:
#     print("no it doesn't")
"""
Exercise 8: Rename key of a dictionary
Write a program to rename a key city to a 
location in the following dictionary.

"""
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# sample_dict['location'] = sample_dict.pop('city')
# print(sample_dict)
"""
Exercise 9:
Get the key of a minimum value 
from the following dictionary
"""
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
# print(min(sample_dict))
"""
Exercise 10
Write a Python program to 
change Brad’s salary to 8500 in the following dictionary
"""
# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }
# sample_dict["emp3"] = {'name': 'Brad', 'salary': 8500}
# print(sample_dict)
