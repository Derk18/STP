import random


users_answer = input("Say YES for a lotto numbers: ")

if users_answer == "Yes" or "yes" or "YES":
    number_1 = random.randrange(1, 52)
    number_2 = random.randrange(1, 52)
    number_3 = random.randrange(1, 52)
    number_4 = random.randrange(1, 52)
    number_5 = random.randrange(1, 52)
    number_6 = random.randrange(1, 52)
    print(number_1)
    print(number_2)
    print(number_3)
    print(number_4)
    print(number_5)
    print(number_6)
    print("Good luck")
else:
    print("HAVE A GOOD DAY ")
    quit()

