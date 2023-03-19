#import random
#random_integer = random. randint(1, 12)
#print(random_integer)

#random_float = random.random() * 5
#print(random_float)

#student_of_statistics= ["Ali", "Farooq", "Muzammil", "Ziad", "Zamir", "Wahid", "amar", "Manahil"]

#student_of_statistics[4]="diary"
#print(student_of_statistics)

#student_of_statistics.append("Marhaba")
#print(student_of_statistics)

#import random
#names_string= input("Give me everybody's names separated by comma")

#names = names_string.split(",")
#num_items=  len(names)
#random_number= random.randint(0, num_items-1)
#person_who_will_pay = names[random_number]
#person_who_will_pay = random.choice(names)
#print(person_who_will_pay + " is going to pay the bill.")


# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen[1][2])
# print(dirty_dozen[1][3])


# import random
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# game_images = [rock, paper, scissors]
# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor. \n"))
# if user_choice>=3 or user_choice<0:
#     print("You typed an invalid number, You lose!")
# else:
#     print(game_images[user_choice])
# computer_choice = random.randint(0,2)
# print(f"Computer chose:")
# print(game_images[computer_choice])



# if user_choice == 0 and computer_choice== 2:
#     print("You win!")
# elif computer_choice > user_choice:
#     print("You lose")
# elif computer_choice == user_choice:
#     print("it's draw")



# elif computer_choice == 0 and user_choice==2:
#     print("You lose")
# elif user_choice > computer_choice :
#     print("You win!")























