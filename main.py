"""
Exercise 1: Guess the number
Exercise 2: Multiplication table
Exercise 3: Basic calculator
"""

import random

def adivina_numero():
    numero_aleatorio = random.randint(1, 10)
    while True:
        try:
            intento = int(input("Adivina el número (entre 1 y 10): "))
            if intento < 1 or intento > 10:
                print("Por favor, ingresa un número entre 1 y 10.")  
            if intento == numero_aleatorio:
                print(f"Has adivinado el número {numero_aleatorio}.")
                break
            else:
                print("Número incorrecto, sigue intentándolo")
        except ValueError:
            print("Por favor, ingresa un número válido.")

    adivina_numero()
#poner numero y continuar,



"""
    Using loops, implement a guessing game.
    Guess the number (1-10):
    messages: Too low, Too high, Try again, Congratulations!
  """
  # fix code
print("Guess the number (1-10):")


def multiplication_table():
  """
    Using a while/for loops, implement a multiplication table.
  """
  # fix code
  print("multiplication_table for {number}")


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