#Python has Strings, Integers, Floats and Boolean data types

# when we want to pull out a character, counting starts from 0, 
#String
city = "Helsinki"
# it will print "l" because the position of l is at third, counting from 0
print(city[2])
numbers_as_string = "12345"
numbers_as_string_1 = "6789"
#it will print nr 123456789
print(numbers_as_string + numbers_as_string_1)

#Integer
nr_as_integers= 12
nr_as_integers_1 = 34
# it will print sum of two nummbers (46)
print(nr_as_integers + nr_as_integers_1)
# len() can not be used with Integers only with Strings
 
# to use , commas as in UK or US, nummbers can be separated with underscore
# for instance 123_456_789 just for us so we can easy read them. The python will remove underscores 
print(123_456_78)

#Float data type
float_number = 9.99888
print(float_number)

number = 567
number2 = float(number)
print(number2)
# converting string to floating number
string_nummber = "567"
float_number = float(string_nummber)
print(float_number + 100)

#Boolean data types 
True 
False

#checking the type of data is done with type()
# String convertion using str() so it can be concatenated 
city = len(input("Where do you live? "))
#another form to convert into string is to save in another variable 
string_city = str(city)
print(type(city))
print('Your city has ' + str(city) + ' characters')

# Subscripting two numbers
nr = input("Enter a two digit number: ")
first_nr = nr[0]
second_nr = nr[1]
# adding nr after extracting each digit. Converting to float from string.
result = float(first_nr + second_nr)
print(type(result))
print(result)

# Calculating, dividing is float 
print(2+ 3)
print(2-3)
print(2*3)
print(2**2) #power 
# Pendas, = first starts with parantheses (), then exponents **, multiplication *, division /, addition +, substraction -, and from left to right. 

result = (4*4 + 4 / 4 - 4)
#prints 13.0 => 16 + 1 - 4
print(result)

# calculating bmi 
h = input('Enter height in metter: ')
w = input('Enter weight in kg: ')
height = float(h)
weight = float(w)
bmi = weight/(height*height)
# printing only full number, 
print(int(bmi))
# rounding the number 2 digits after decimal point. 
print(round(bmi, 2))

# floor division, will print 2. 
print(9//4)  

points = 8 
# adding 1 point, short form 
points += 1
# substracting 1 point, 
points -= 1
# mulitplying by 2 points, 
points *= 2

# boolean value
is_on = True
# f-String 
print(f"your points are {points}, your bmi is {bmi} and it is on {is_on}")

# calculate a long time project 
project = input("How many years are past in the project? ")
project_int = int(project)
years_remaining = 20 -project_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
remain=  f" You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months, {years_remaining} years remaining"
print(remain)

# calculating restaurant bill 
bill = input("What is total bill? ")
tip = input('Choose tip you want to give such as 10, 15 or 20%: ')
nr_of_people = input('Enter nr of people: ')

sum_to_pay = float(bill)*(1 + (float(tip))/100)/ float(nr_of_people)

print(f" sum to pay is {sum_to_pay}")