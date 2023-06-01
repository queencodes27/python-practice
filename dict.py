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
Exercise 7: Check if a value exists in a dictionary
"""
sample_dict = {'a': 100, 'b': 200, 'c': 300}
