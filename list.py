"""
Exercise 1: Reverse a list in Python
"""
# list1 = [100, 200, 300, 400, 500]
# list1.reverse()
# print(list1)

"""
Exercise 2: Concatenate two lists index-wise
Write a program to add two lists index-wise. 
Create a new list that contains the 0th index item 
from both the list, then the 1st index item, 
and so on till the last element. any leftover items will get added at the end of the new list.

"""
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]


# list1 = ["M", "na", "i", "Ke"] 
# list2 = ["y", "me", "s", "lly"]
# list3 = [i + j for i, j in zip(list1, list2)]
# print(list3)

"""
Exercise 3: Turn every item of a list into its square
Given a list of numbers. 
write a program to turn every item of a list into its square.

"""
# numbers = [1, 2, 3, 4, 5, 6, 7]
# list =[]
# for i in numbers:
#     list.append(i * i)
# print(list)
"""
Exercise 4: Concatenate two lists in the following order
"""

# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]

# result = [x + y for x in list1 for y in list2]
# print(result)
"""
Exercise 5: Iterate both lists simultaneously
Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.


"""
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]

# for x, y in zip(list1, list2[::-1]):
#     print(x, y)
"""
Exercise 6: Remove empty strings from the list of strings
"""

# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# list2 = list(filter(None, list1))
# print(list2)
"""
EX 8:
Write a program to add item 7000 after 
6000 in the following Python List
"""
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)
"""
EX 9
You have given a nested list. Write a program to extend it by adding the sublist ["h", "i", "j"] in such a way that 
it will look like the following list.
"""
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub_list = ["h", "i", "j"]
# list1.extend(sub_list)
# print(list1)
"""
EX 10
Given a Python list, write a program to remove all occurrences of item 20.
"""
# list1 = [5, 20, 15, 20, 25, 50, 20]
# remove_item = 21
# for item in list1:
#     if (item == remove_item):
#         list1.remove(remove_item)
# print(list1)


