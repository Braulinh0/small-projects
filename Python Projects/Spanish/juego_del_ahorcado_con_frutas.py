# Importamos choice para hacer eleccion aleatoria de frutas

from random import choice

# ---------------------------------------------------------------

# Creamos múltiples opciones de frutas para seleccionar de forma aleatorio

def eleccion():
    opciones = ["manzana", "frutilla", "durazno", "naranja", "kiwi", "platano", 
                "mango", "granada", "melon", "sandia", "mandarina", "limon", "uva",
                "cereza", "piña", "maracuya", "mora", "frambuesa", "ciruela", 
                "papaya", "pera", "coco", "chirimoya", "higo", "zarzamora", "pomelo",
                "melocoton", "albaricoque"]
    return choice(opciones) # Se retorna la palabra escogida de forma aleatoria.

# ---------------------------------------------------------------

# Revisamos si la palabra seleccionada por el usuario ya fue utilizada anteriormente.

def ya_elegida(c, lista) :
    if c in lista :
        return True
    else :
        lista.append(c)
        return False

# ---------------------------------------------------------------

# Después, comprobamos si la letra selecionada por el usuario se encuentra dentro de la palabra oculta.

def comprobar_letra(palabra, c, progreso) :
    encontrada = False # <- Para comprobar si aparece al menos una vez dentro de la palabra. 
                       # Ya que si no aparece una letra al menos entonces se le restará una vida al jugador.
                       
    progreso_nuevo = list(progreso) # <- Sirve para almacenar las letras descubiertas de la palabra oculta.
    contador = 0 # <- Los carácteres que se le restará al total de palabra que quedan sin descubrir.
    
    for i in range(len(palabra)) :
        if palabra[i] == c and progreso[i] == '_':
            progreso_nuevo[i] = c
            encontrada = True
            contador += 1
            
    # Retornamos si hay al menos una letra igual a la letra ingresada por el usuario, el nuevo 
    # Progreso de palabras ocultas y el contador restará al total de letras sin descubrir.
    return encontrada, "".join(progreso_nuevo), contador 
    
# ---------------------------------------------------------------

palabra = eleccion()
progreso = '_' * len(palabra)
letras_usadas = [] # <- Registro de palabras ya utilizadas por el usuario.
vidas = 6 # <- Puedes editar esto para que el juego sea más duradero o no.
letras_restantes = len(palabra) # <- Total de letras sin descubrir aún.

while vidas != 0 :
    print(f"\nPalabra: {progreso}") # <- Muestra el progreso que llevas descubierto de la palabra misteriosa.
    print(f"Vidas: {vidas} | Letras usadas: {sorted(letras_usadas)}") # <- Vidas del jugador y letras usadas.
    print(f"Letras restantes: {letras_restantes}") # <- Total de letras sin descubrir aún.
    
    letra = input("Ingresa una letra: ").lower()
    
    if ya_elegida(letra, letras_usadas) :
        print("Ya has elegido esta letra, selecciona otra.")
        continue

    acierto, progreso, resta = comprobar_letra(palabra, letra, progreso)
    
    if acierto : # <- Si acertaste al menos una letra de la palabra misteriosa.
        print("¡Acertaste!")
        letras_restantes -= resta
    else : # <- Si no acertaste.
        print("Esta letra no está...")
        vidas -= 1
        
    if "_" not in progreso : # <- Se revisa si ya no hay carácteres por descubrir.
        print(f"¡Has ganado, felicidades! La palabra era: {palabra}")
        break
    
if vidas == 0 :
    print("¡Has perdido! La palabra era: {palabra}")
