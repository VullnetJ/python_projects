
# conditions 

weather_heat = int(input("Enter weather in Celcius: "))
if weather_heat >= 40:
    print('Stay indoors')
else: 
    print("You are free to go outside")

# checking if the number is odd or even

nr_check = int(input("Enter your number: "))

if nr_check % 2 == 0: 
    your_lucky_nr = int(input('Write a positive or negative number: '))
    if your_lucky_nr >= 0:
        print("The number is even and you prefer positive nr")
    else: 
        print("The number is even and you prefer negative nr")
else:
    print("The number is odd")


# calculating bmi with condition
h = input('Enter height in metter: ')
w = input('Enter weight in kg: ')
height = float(h)
weight = float(w)
bmi = weight/(height*height)
print(bmi)

if bmi < 18.5: 
    print('You are underweight')
elif bmi <25: 
    print(" you have a normal weight")
elif bmi <30:
    print("you are overwieght")
elif bmi <35: 
    print('You are over weight limit')

# calculating leap year, one year that is evenly divisible by 4 and reminder 0, except is divisible by 100, unless divisible by 400

year = int(input('Enter the year: '))

# if remainder is 0 it means it is a leap year. 
if year% 4 == 0:
    if year % 100 == 0: 
        if year % 400 == 0:
           print(" It is a leap year")
        else: 
            print("It is not a leap year")
    else: 
        print('Its a leap year')
        
else:  
    print("It is not a leap year")

# ordering coffee 

coffee_price = 5
wants_coffee = input("Do you want coffee? write Yes or No ")
if wants_coffee == "Yes": 
    print(f"You have to pay: {coffee_price}")
else: 
    print("You dont have to pay coffee")

# ordering pizza home
pizza_size = input("Choose the pizza size, Small, Medium or Large")
add_spicies = input("Add spicies? Yes or No")
extra_cheese = input("Do you want extra cheese in pizza ? Yes or No")

bill = 0 
if pizza_size == 'Small': 
    bill += 10 
elif pizza_size == "Medium":
    bill +=12
elif pizza_size == "Large": 
    bill += 15

if add_spicies == "Yes": 
    if pizza_size == "Small":
        bill +=3 
    else: 
        bill += 4

if extra_cheese == "Yes":
    bill +=2
print(f"You have to pay ${bill}")

# logical operator a, b 
x = 10 
y = 12, 
#x > y # False 
#x > 9 and y > 9 # True
# not operator, reverses the operator
not x > 20 # True


#Matching Calculator
name = input("Write your name \n")
name1 = input("Write your name \n")

lower_case = (name + name1).lower()
t = lower_case.count('t')
r = lower_case.count('t')
u = lower_case.count('t')
e = lower_case.count('t')
true = t + r + u + e 


l = lower_case.count('t')
o = lower_case.count('t')
v = lower_case.count('t')
e = lower_case.count('t')

love = l + o + v + e
scores = int(str(true) + str(love))

if scores < 10 or scores > 90:
    print(f"Your score is {scores} , you go together")
elif scores >= 40 and scores <= 50: 
     print(f"Your score is {scores} , you are alright together")
else: 
    print(f"Your score is {scores}")

# decision gaming
print("Travelling destination")
choice1 = input('You\re at a crossroad, where do you want to go? Write "left" or "right" ').lower()


if choice1 == "right":
    choice2 = input('You\'ve come to a river. Type "bridge" if you want to go to the bridge. Type "swim" if you want to swim').lower()
    if choice2 == "bridge":
        choice3 = input('You passed the river and there is a house with two doors. Choose which door you enter. write "Blue" or "White"').lower()
        if choice3 == 'white':
            print("you win")
        elif choice3 == "blue":
            print('Game over')
    else: 
        print("Game Over, you can not swim in the river. ")

else: 
    print("You fell into a trap. Game Over for you")