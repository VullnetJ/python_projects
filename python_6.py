
# functions. 
import random
import math
def function():
    print("Hi there!")
def dosmth():
    print("Doing something")
for step in range(2): 
   dosmth()

#choosing random letters, comparing random words with random letter if it matches
words = ["Stockholm", "Helsinki", "Tirana", "Athens"]
chosen_word = random.choice(words)


# replacing letters 
end_game = False
display = []
word_length = len(chosen_word)
while not end_game:
    guessing = input("Geuss a letter: ").lower()

  
    # for letter in range(len(chosen_word)):
    #     display += "_"
    # print(display)


    for l in range(word_length):
        letter = chosen_word[l]
        if l == guessing:
            display[l] = letter
            print("It matches")
        # else:
        #     print("Not match")
    if "_" not in display:
        end_game = True
        print("You won ")

# calculating surface, color needed to paint wall. 
height_h = int(input("Height of wall: "))
width_w = int(input("Width of wall: "))
coverage_per_can = 5 

def paint_needed(height, width, cover):
    area = height * width
    nr_of_cans = math.ceil(area/cover)
    print(f"There are needed {nr_of_cans} cans to paint")

paint_needed(height=height_h, width=width_w, cover=coverage_per_can)