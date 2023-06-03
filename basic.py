"""
Exercise 1: Calculate the multiplication and sum of two numbers
Given two integer numbers return their product only if the product is equal to or lower than 1000, 
else return their sum.

"""
# number1 = 20
# number2 = 30
# if number1 * number2 <= 1000:
#     print (number1 * number2)
# else:
#     print(number2 + number1)

# number1 = 40
# number2 = 30
# if number1 * number2 <= 1000:
#     print (number1 * number2)
# else:
#     print(number2 + number1)

# # FUNCTION
# def product_or_sum(num1, num2):
#     product = num1 * num2
#     if product <= 1000:
#         return product
#     else:
#         return num1 + num2
# print(product_or_sum(20, 30))
# print(product_or_sum(40,30))



"""
Exercise 2: Print the sum of the current number and the previous number
Write a program to iterate the first 10 numbers and in each iteration, print the sum of the 
current and previous number.

"""
# prev_num = 0
# for i in range (0, 10):
#     # sum = prev_num + i
#     print(f"Current num {i}", "Previous num :", i - 1 ,"sum: ", prev_num + i + prev_num  )
    
"""
Exercise 3: Print characters from a string 
that are present at an even index number
"""

# word = str(input("enter word "))
# even_index = []
# for i in range(len(word)):
#     if i % 2 == 0:
#         even_index.append(word[i])
#     else:
#         print("none")

"""
Exercise 4: Remove first n characters from a string

"""
# str = input(" enter word:") 
# list = []
# for i in range(0, len(str)):
#     if i % 2 == 0:
#         a = str[i]
#         list.append(a)
#     else:
#         pass
"""
Exercise 5: Check if the first and last number of a list is the same
Write a function to return 
True if the first and last number of a given list is same. 
If numbers are different then return False.
"""
# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]

# def same(list):
#     print("l: ", list)
#     first_num = list[0]
#     last_num = list[-1]
#     if first_num == last_num:
#         return True
#     else:
#         return False
# print("result is", same(numbers_x))
# print("result is", same(numbers_y))

"""
Exercise 6: Display numbers divisible by 5 from a list
Iterate the given list of numbers and print only those 
numbers which are divisible by 5

"""
# givenlist = [10, 20, 33, 46, 55]
# for i in givenlist:
#     if i % 5 == 0:
#         print(i)
"""
Write a program to find how many times substring “Emma” appears in the given string
"""
# str_x = "Emma is good developer. Emma is a writer"
# list = str_x.count("Emma")
# print(list)
