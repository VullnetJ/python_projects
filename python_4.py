import random
# generating random number

random_nr = random.randint(10, 100)
random_nr2 = random.random() *4
print(random_nr)
print(random_nr2)

#head and tails generating game. 
random_flip = random.randint(0,1)
if random_flip == 0:
    print("Tails")
else:
    print("Head")

# lists 
fruits = ['apple', 'orange', 'grape']
# print the first item
print(fruits[0])
# taking the last element from the list
print(fruits[-1])
# modifying list. 
fruits[0] = 'cherry'
# add an item to the list at the end. 
fruits.append("pear")

# printing random names of the fruits, 
random_fruits = random.randint(0, len(fruits) -1)
print(fruits[random_fruits])

# extending the list with many items
fruits.extend(['kiwi', 'hazzelnut'])

# splitting strings into separate components 
text = 'Hello from Helsinki'
split = text.split(',')

print(split)
vegetables = ['tomato', 'celery', 'spinach']
nested_list = [fruits, vegetables]
print(f'Nested list:  {nested_list}')

# treasure game
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
print(f"{row1}\n{row2}\n{row3}")
map = [row1, row2, row3]
position = input("Which is the treasure position ")

horizontal = int(position[0])
vertical = int(position[1])
selected_row = map[vertical -1][horizontal -1 ] = "*"
print(f"{row1}\n{row2}\n{row3}")


# Rock Paper Scissors ASCII Art

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
img = [rock, paper, scissors]

u_choice = int(input("Choose 0 for Rock, 1 for Paper, 2 for Scissors: \n"))
print(img[u_choice])

if u_choice >=3 or u_choice <0:
    print("You typed invalid number, bye bye")
else:
    random_comp_choice = random.randint(0,2)
    print(f"Computer chose: ")
    print(img[random_comp_choice])

    if u_choice == 0 and random_comp_choice == 2: 
        print("You win")

    elif random_comp_choice > u_choice:
        print("You lost, game over")
    elif u_choice > random_comp_choice:
        print("You win")
    elif random_comp_choice == u_choice:
        print("It's a draw")
    elif random_comp_choice == 0 and random_comp_choice == 2:
        print("You loose")
