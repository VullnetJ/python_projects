from random import *
import base64
import time
import threading


user_pass = input("enter your password: ")

password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y', 'z']

guess = ''
guess1 = ''

length = len(user_pass)
l1 = user_pass[0:1]
l2 = user_pass[1:2]


while guess != l1:
    guess = ""
    for letter in range(len(l1)):
        guess_letter = password[randint(0, 25)]
        guess = str(guess_letter) + str(guess)
    print(f"Guess is: {guess}")
print("Matched first letter password is: ", guess)


while guess1 != l2:
    guess1 = ""
    for letter in range(len(l2)):
        guess_letter = password[randint(0, 25)]
        guess1 = str(guess_letter) + str(guess1)
    print(f"Guess is: {guess1}")

print("Matched second letter password is: ", guess1)

print(f"Fully matched is: {guess + guess1}")

# def eat():
#     time.sleep(5)
#     print("You eat 5 seconds")

# def drink():
#     time.sleep(3)
#     print("You drink 3 seconds")

# def study():
#     time.sleep(5)
#     print("You study 5 seconds")

# x = threading.Thread(target = f1, args=())
# x.start()

# y = threading.Thread(target = f2, args=())
# y.start()







# z = threading.Thread(target = study, args=())
# z.start()


# eat()
# drink()
# study()







# slicing = guess[0]
# slicing1 = guess[1]

# running threading. and target= a function. 
# t1 = threading.Thread(target=slicing)
# t2 = threading.Thread(target=slicing)

# t1.start()
# t2.start()

# # the script 
# t1.join()
# t2.join()

# throw away variable, we are not using in the loop 
# threads = []

# for _ in range(2):
#     t = threading.Thread(target=slicing)
#     t.start()
#     threads.append(t)
# for thread in threads: 
#     thread.join() 

print(f"number of threading {threading.active_count()}")
print(f"number of enumerate {threading.enumerate()}")
print(f"performance counter {time.perf_counter()}")

# user_pass = user_pass.encode("utf-8")
# encoded = base64.b64encode(user_pass)
# print(f"Encoded password {encoded}")
# decoded = base64.b64decode(encoded)
# print(f'decoded password: {decoded}')