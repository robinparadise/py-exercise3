import random

def adivina_numero():
    numero_aleatorio = random.randint(1, 10)
    while True:
        try:
            intento = int(input("Adivina el número (entre 1 y 10): "))
            if intento < 1 or intento > 10:
                print("Por favor, ingresa un número entre 1 y 10.")
                continue
            
            if intento == numero_aleatorio:
                print(f"Has adivinado el número {numero_aleatorio}.")
                break
            else:
                print("Número incorrecto, sigue intentandoló")
        except ValueError:
            print("Por favor, ingresa un número válido.")

adivina_numero()