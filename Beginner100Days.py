"""Coffee program"""

"""Sets of all the programs produced in the 100 day challenge from beginner to intermediate!"""

"""DAY 1 Project: BAND NAME GENERATOR"""
# # Must create a greeting
# # Ask user city they grew up in
# # Ask user their pet name
# # Combine pet name + city
#
# a = int("5") / int(2.7)
# print(type(a))
# # improvisation >> Combine pet name + city name + name and return the new name
#
# import random
#
# # Name = random.choice(['Aria ', 'Maria ', 'Mini-Aria ', 'Jackson ', 'Mark ', 'Allen ', 'Chandler ', 'Ridwandr '])
# #
# # CityName = random.choice(['Chicago ', 'NewRussia ', 'Woodbridge ', 'Asgard '])
# #
# # PetName = random.choice(['DiuDiu ', 'Martz ', 'Lillian ', 'Lila ', 'xiaoluo ', 'sally '])
# #
# # BandName = Name + CityName + PetName;
# # print("Your new band name is " + BandName)
# #
# # # Try this! // works with integers
# #
# # Two_Digit_Number = input("Enter a two digit value ")
# #
# # First_Digit = Two_Digit_Number[0]
# # Second_Digit = Two_Digit_Number[1]
# #
# # Multiplcation = int(First_Digit) * int(Second_Digit)
# # print(Multiplcation)
# #
# # # PEMDAS parenthesis (), add + , subtract -, multiplication *, division /, exponent **,
# #
# # """BMI CACLULATOR"""
# #
# # height = input("Enter the height in m ")
# # weight = input("Enter the weight in kg ")
# #
# # # Given that the BMI is computed by weight/height^2
# # # note: // creates a new int type for division.
# # # note2: % used to determine the modular or remainder of a value.
# #
# # BMI = int(weight) / (float(height) ** 2)
# # bmi_as_int = round(BMI, 2)
# #
# # if bmi_as_int < 18.5:
# #     print(f"underweight {bmi_as_int}")
# # elif bmi_as_int >= 18.5 and bmi_as_int <= 24.9:
# #     print(f"normal weight {bmi_as_int}")
# # elif bmi_as_int >= 25 and bmi_as_int <= 29.9:
# #     print(f"overweight {bmi_as_int}")
# # elif bmi_as_int > 30 and bmi_as_int < 35:
# #     print(f"Obese {bmi_as_int}")
# # else:
# #     print(f"Clinically obese {bmi_as_int}")
# #
# # # f-string is allows various data type to be printed out in the same statement. i.e print(f"xxxx {datatype}"?
# #
# # PersonAge = input("enter your current age ")
# # MaximumAge = 90;
# # DayInAYear = 365;
# # WeeksInAYear = 52;
# # MonthsInAYear = 12;
# #
# # MonthsLeft = (MaximumAge - int(PersonAge)) * 12
# # DaysLeft = (MaximumAge - int(PersonAge)) * 365
# # WeeksLeft = (MaximumAge - int(PersonAge)) * 52
# # # if current age = 3, the months until you hit 90 = (90 - 3) * 12
# # # if current age = 3, the weeks until you hit 90 = (90 - 3) * 52
# # # if current age = 3, the days until you hit 90 = (90 - 3) * 365
# # message = f"You have {DaysLeft} days, {WeeksLeft} weeks, and {MonthsLeft}"
# # print(message)
# #
# # """Day 2 Project : Tip Calculator"""
# # # Tip calculator!
# # print("Welcome to the tip calculator! ")
# # TotalBill = float(input("What was the total bill **Cost? $"))
# # TipAmount = int(input("Please input the amount of tip, 10%, 15%, 20%, 25%, 30%, or a custom amount "))
# # BillSplit = int(input("How many people to split the bill? "))
# # TipInBill = TipAmount / 100 * TotalBill + TotalBill
# #
# # TipInBill_PerPerson = TipInBill / BillSplit
# # Finalamount = round(TipInBill_PerPerson, 2)
# # print(f"Each person pays ${Finalamount}")
# # #
# #
# # # Day 3 project exercise odd or even
# #
# # number = int(input("Enter a value that you want to determine whether odd or even"))
# # if number % 2 == 0 and number != 0:
# #     print("The following is even")
# # else:
# #     print("The following is odd")
# #
# # # Determine whether the following year is a leap year or not
# #
# # SomeYear = int(input("Enter the current year!"))
# #
# # if SomeYear % 4 == 0:
# #     print("Leap year")
# #     if (SomeYear % 100 == 0):
# #         if (SomeYear % 400 == 0):
# #             print("Is a leap year")
# #         else:
# #             print("Not Leap Year")
# #     else:
# #         print("Leap year")
# # else:
# #     print("Not a leap year")
# #
# # # Roller coaster eligibility
# #
# # RollerHeight = int(input("Enter your height in cm"))
# #
# # if RollerHeight >= 120:
# #     print("You are able to ride the roller coaster! ")
# # else:
# #     print("Not able to ride roller coaster! Too short! ")
# #
# # # Coding exercise day 3.4 Pizza order!
# #
# # print("Welcome to the pizza shop ")
# # size = input("Enter the size! S, M, L, XL, XXL ")
# # add_pepperoni = input("Do you want to add pepperoni? Y, N")
# # add_cheese = input("Do you want to add chess? Y, N ")
# #
# # initialBill = 0
# # if size == "S":
# #     initialBill += 15
# #     print("Price is $15 ")
# # elif size == "M":
# #     initialBill += 20;
# #     print("Price is $20 ")
# #
# # elif size == "L":
# #     initialBill += 25
# #     print("Size is $25 ")
# # else:
# #     initialBill += 25
# #
# # if add_pepperoni == "Y":
# #     if size == "S":
# #         initialBill += 2
# #     else:
# #         initialBill += 3
# #
# # if add_cheese == "Y":
# #     initialBill += 1
# #
# # print(f"Your final bill is ${initialBill}")
# #
# # # Exercise 3.5 Love Calculator!
# #
# # print("Welcome to the love calculator")
# # Person1Name = input("Please provide me your name ")
# # Person2Name = input("Please provide me their name ")
# #
# # """"DAY 3 FINAL PROJECT: Treasure Island!"""
# #
# # print("Your purpose is to find treasure island! ")
# # choice1 = input('\'Which direction would you like to go? Type "left" or " right".').lower()
# #
# # if choice1 == "left":
# #     choice2 = input(
# #         "You've come across the edge of the island, you discover 3 doors. On your left, you see a red door. \n On your right, you see a black door. \n In the middle you see a green door").lower()
# #     if choice2 == "red":
# #         choice3 = input(
# #             "As you enter the door, you discover that there are treasures of unimaginable power. \nYou see two doors behind the treasure. Do you proceed or do you enter the right or left door?").lower()
# #         if choice3 == "proceed":
# #             print("You have gained unimaginable power! ")
# #         else:
# #             print("Gameover!")
# #             if choice2 == "black":
# #                 choice3 = input(
# #                     "As you enter the door, you discover that There is a corpse that holds a scripture. \n Do you proceed to take it or will you respect the dead? ").lower()
# #                 if choice3 == "proceed":
# #                     choice4 = input(
# #                         "Your mind begin to collect the information from the scripture simply by absorbing it into your body. \n You have now exploded into thousands of pieces. \n proceed if you wish to mangle back you body ").lower()
# #                     if choice3 == "proceed":
# #                         print(
# #                             "You have won the game! You found the treasure! The ability to reshape your body and bring yourself back to life. \n The one and only holy item! ").lower()
# #                     else:
# #                         print("Gameover! You decided to pass away and not reshape your body ")
# # else:
# #     print("Gameover")
# #
# # # Day 4 Heads or tails exercise using random
# #
# # number = random.randint(1, 2)
# # if number == 1:
# #     print("heads")
# # else:
# #     print("tails")
#
# # Day 4 nank roulette exercise
#
# names_stirngs = input("Give me the list of names of everybody. ")
# names = names_stirngs.split(", ")
#
# num_items = len(names)
# payer = random.randint(0,num_items - 1);
# print(payer)
#
# if payer == names[0]:
#     print("you are paying! ")
# else:
#     print("You are not the payer. ")
#
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#
# dirty_dozen = [fruits, vegetables]
#
# print(dirty_dozen[1][1])
#
# # Day 4.3 Treasure Map exercise
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
#
# horizontal = int(position[0])
# vertical = int(position[1])
#
# selected_row = map[vertical-1]
# selected_row[horizontal - 1]
# map[vertical-1][horizontal -1] = 'X'
# print(f"{row1}\n{row2}\n{row3}")
#
# # Final project for day 4
#
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
# game_images = [rock, paper, scissors]
#
# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# print(game_images[user_choice])
#
# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])
#
# if user_choice >= 3 or user_choice < 0:
#   print("You typed an invalid number, you lose!")
# elif user_choice == 0 and computer_choice == 2:
#   print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#   print("You lose")
# elif computer_choice > user_choice:
#   print("You lose")
# elif user_choice > computer_choice:
#   print("You win!")
# elif computer_choice == user_choice:
#   print("It's a draw")
#
# ####### Debugging challenge: #########
# #Try running this code and type 5.
# #It will give you an IndexError and point to line 32 as the issue.
# #But on line 38 we are trying to prevent a crash by detecting
# #any numbers great than or equal to 3 or less than 0.
# #So what's going on?
# #Can you debug the code and fix it?


#Day 5 Python loops Create a password generator

# newFruit = ["apple", "cake", "cookies"]
# for fruit in newFruit:
#     print(fruit)

# Day 5 height exercise.

# student_heights = input("Input a list of student height ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
#
# StudentHeight = 0
# for student_height in student_heights:
#     StudentHeight += student_height
# print(StudentHeight)
#
# numstudent = 0
# for students in student_heights:
#     numstudent += 1
# print(numstudent)
#
# averageHeight = round(StudentHeight/numstudent)
# print(averageHeight)

#Day 5.2 Highscore exercise
#
# student_scores = input("Enter your student scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
#
# counter = 0
# for score in student_scores:
#     if score > counter:
#         counter = score
# print(f"The highest score in the course is {counter}")


# counter = 0
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         # divisible by 3
#         print("fizzbuzz!")
#     elif number % 3 == 0:
#         print("fizz!")
#     elif number % 5 == 0:
#         print("buzz")
#     else:
#         print(number)


#Day 5 Project password generator
# import random
#
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# n_letters = int(input("Enter the number of letters you would like! "))
# n_symbols = int(input("Enter the number of symbols you would like! "))
# n_numbers = int(input("Enter the number of numbers you would like! "))
#
# passwordGenerated = []
#
# for char in range(1, n_letters + 1):
#     passwordGenerated.append(random.choice(letters))
#
# for char in range(1, n_symbols + 1):
#     passwordGenerated.append(random.choice(letters))
#
# for char in range(1, n_numbers + 1):
#     passwordGenerated.append(random.choice(letters))
#
# print(passwordGenerated)
# random.shuffle(passwordGenerated)
# print(passwordGenerated)
#
# password = ""
# for char in passwordGenerated:
#   password += char
#
# print(f"Your password is: {password}")
#

Penny = 0.01
Dime = 0.1
Nickel = 0.05
Quarter = 0.25
NumPenny = int(input("How many pennies? "))
NumDime = int(input("How many dimes? "))
NumNickel = int(input("How many nickels? "))
NumQuarter = int(input("How many quarters? "))

TotalAmount = round((NumPenny * Penny + NumDime * Dime + NumNickel * Nickel + NumQuarter * Quarter), 2)
print(TotalAmount)

