letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random

password_list = []

for l in range(0, nr_letters):
    nr_letters_random = random.choice(letters)
    password_list.append(nr_letters_random)
for s in range(0, nr_symbols):
    nr_symbols_random = random.choice(symbols)
    password_list.append(nr_symbols_random)
for n in range(0, nr_numbers):
    nr_numbers_random = random.choice(numbers)
    password_list.append(nr_numbers_random)

print(password_list)
random.shuffle(password_list)
print(password_list)

temp = ""
for i in password_list:
    temp+= i
print(f"Your password is : {temp}")