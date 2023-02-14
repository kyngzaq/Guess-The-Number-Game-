import random

number = random.randint(1,10)
for i in range(0,3):
    print("From 1 - 10")
    user = int(input("guess the number: "))
    if user == number:
        print("Hurray!!")
        print(f"you guessed the Number right it's {number}")
        break
if user != number:
    print(f"Your guess is incorrect the Number is {number}")