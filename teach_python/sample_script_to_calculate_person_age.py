print("Welcome to Introduction to Python!")

name = input("What is your name? ")

print("Hello,", name + "!")

birth_year = input("What year were you born? ")
age = 2024 - int(birth_year)

print("You are approximately", age, "years old.")

if age >= 18:
    print("You are old enough to vote!")
else:
    print("You are not old enough to vote yet.")
