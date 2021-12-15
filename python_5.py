import string
from string import punctuation
import random

# looping through
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
for fruit in fruits: 
    print(fruit)
    print("Apple pie + " + fruit)
    print(fruits)
# calculating average
kilogram = [60, 78, 89, 80, 68, 68, 98]

#length = len(kg)
#print(sum(kg)/length) 
total_kg = 0
length = 0

for kg in kilogram:
    total_kg += kg
    length += 1
average = round(total_kg/ length, 2)

print(f"average is {average}")

# max max(kilogram)
max_v = 0
for k in kilogram: 
    if k > max_v: 
        max_v = k 
print(f"The kg with highest is: {max_v}")

# min 
min_v = 0
for k in kilogram: 
    if k < min_v: 
        min_v = k 
print(f"The kg with highest is: {min_v}")

# using for loops with a range, 4 is step side
total = 0
for item in range(1, 100, 4):
    total += item
print(total)

# adding even numbers 
even_nr_sum = 0 
for number in range(1, 101, 2): 
    if number % 2 == 0: 
        even_nr_sum += number
print(even_nr_sum)

# fizzbuzz game 
for nr in range(1, 51):
    if nr % 3 == 0 and nr % 5 == 0:
        print("FizzBuzz")
    elif nr %  3 == 0:
        print("Fizz")
    elif nr % 5 == 0:
        print("Buzz")
    else:
        print(nr)
# Generating strong password 
letters_lower = list(string.ascii_lowercase)
letters_upper = list(string.ascii_uppercase)


numbers = ['1','2','3','4','5','6','7','8','9','0']


special_characters = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']


print("Generate Strong Password")
number_of_letters = int(input("Type number of letters you want in password? \n"))
number_of_numbers = int(input("Type number of numbers you want in password? \n"))
number_of_symbols = int(input("Type number of symbols you want in password? \n"))

# # doing in a simply way and more complicated 
# password = ""

# for p in range(1, number_of_letters + 1):
#     random_character = random.choice(letters_upper)
#     password += random_character
#     print(password)
# for p in range(1, number_of_symbols + 1):
#     random_character = random.choice(numbers)
#     password += random_character
#     print(password)
# for p in range(1, number_of_symbols + 1):
#     random_character = random.choice(special_characters)
#     password += random_character
#     print(password)
# print(password)

p_list = []
for p in range(1, number_of_letters + 1):
    random_character = random.choice(letters_upper)
    p_list += random_character

for p in range(1, number_of_symbols + 1):
    random_character = random.choice(numbers)
    p_list += random_character

for p in range(1, number_of_symbols + 1):
    random_character = random.choice(special_characters)
    p_list += random_character
   
print(p_list)
# mixing orders with letters, characters and numbers
random.shuffle(p_list)
print(p_list)

password = ""
for p in p_list:
    password += p
print(f"Your password is {password}")
