# Fruits = ["Apple", "Peach", "Pear" ]
# for fruit in Fruits:
#     print(fruit)
#     print(fruit + "Pie")
# print(Fruits)
# total = 0
# for number in range (2, 102, 2):
#     total += number
# print(total)





# student_heights = input("Input a student list").split()
# for n in range (0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)

# total_height = 0
# for height in student_heights:
#      total_height  += height
# print(total_height)

# number_0f_student = 0
# for student in student_heights:
#      number_0f_student+=1
# print(number_0f_student)

# average_height = round(total_height / number_0f_student)
# print(average_height)






# student_scores = input("Input a student score").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print (student_scores)

# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score= score
# print(f"The highest score in the class is : {highest_score}")




# day - 5 project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ]

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy Level
# password = ""
# for char in range (1, nr_letters+1):
#     password += random.choice(letters)
# for char in range (1, nr_symbols+1):
#     password += random.choice(symbols)
# for char in range (1, nr_numbers+1):
#     password+= random.choice(numbers)
# print(password)



# HArd Level
# password_list = []
# for char in range (1, nr_letters+1):
#      password_list+=random.choice(letters)
# for char in range (1, nr_symbols+1):
#      password_list += random.choice(symbols)
# for char in range (1, nr_numbers+1):
#      password_list+= random.choice(numbers)
# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password = ""
# for char in password_list:
#      password+=char
# print(f"Your password is: {password}")



















