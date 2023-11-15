"""
Exercise 1: Guess the number
Exercise 2: Multiplication table
Exercise 3: Basic calculator
"""

import random

def guess_the_number():
  """
    Using loops, implement a guessing game.
    Guess the number (1-10):
    messages: Too low, Too high, Try again, Congratulations!
  """
  # fix code
input("Guess the number (1-10):")

secret_number = random.randint(1, 10)
    guess = 0

    while guess != secret_number:
        try:
            guess = int(input("Guess the number (1-10): "))
            if guess < secret_number:
                print("Too low, try again.")
            elif guess > secret_number:
                print("Too high, try again.")
            else:
                print("Congratulations! You guessed the right number.")
        except ValueError:
            print("Please enter a valid number between 1 and 10.")

guess_the_number()


def multiplication_table():
  """
    Using a while/for loops, implement a multiplication table.
  """
  # fix code
  input("multiplication_table for {number}")





def basic_calculator():
  """
    Using a while/for loops, implement a basic calculator.
    1. Enter the first number: 10
    2. Enter an operator (+, -, *, /): +
    3. Enter the second number: 20
    4. print 10 + 20 => Result: 30
  """
  num1 = input("Enter the first number: ")
  operator = input("Enter an operator (+, -, *, /): ")
  num2 = input("Enter the second number: ")

  result = None # fix code

  print("{num1} {operator} {num2} => Result:", result)


def main():
  # input choice between 1-3 function
  # call the function
  choice = int(input(f"""
    1. Guess the number
    2. Multiplication table
    3. Basic calculator
    Enter a number (1-3): """))
  if choice == 1:
    guess_the_number()
  elif choice == 2:
    multiplication_table()
  elif choice == 3:
    basic_calculator()
  else:
    print("Invalid choice.")

main()