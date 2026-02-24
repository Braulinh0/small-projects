# Importamos randint desde la librería random para generar números aleatorios

from random import randint

# ---------------------------------------------------------------

numero_secreto = randint(1, 100) # -> Generamos un número secreto aleatorio entre 1 y 100
vidas = 8
encontrador = False

# ---------------------------------------------------------------

while vidas >= 0:
    digito = int(input("\nIngresa un número: "))
    
    if digito < 1 or digito > 100: # -> Verificamos si el número ingresado está fuera del rango permitido
        print("El número ingresado no está permitido.")
    elif digito < numero_secreto: # -> Si el número es menor que el número secreto
        print("Número incorrecto.")
        print("El número elegido es menor que el número oculto.")
        vidas -= 1
    elif digito > numero_secreto: # -> Si el número es mayor que el número secreto
        print("Número incorrecto.")
        print("El número elegido es mayor que el número oculto.")
        vidas -= 1
    elif digito == numero_secreto: # -> Si el número ingresado es igual al número secreto
        print("¡Encontraste el número oculto!")
        print(f"El número oculto era: {numero_secreto}")
        print(f"¡Quedaste con {vidas} vidas restantes!")
        encontrador = True
        break
    
# ---------------------------------------------------------------

if encontrador == False: # -> Si el ciclo terminó y el jugador no encontró el número
    print(f"\n¡Perdiste! El número oculto era: {numero_secreto}")
