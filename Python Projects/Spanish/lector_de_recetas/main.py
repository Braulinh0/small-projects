# ----- Librerías -----

from pathlib import Path
from os import system
import shutil

# ----- Funciones -----

# 1. Lectura de recetas
def leer_receta(base):
    system("cls")

    categorias = [carpeta for carpeta in base.iterdir() if carpeta.is_dir()]

    print("Selecciona una categoría:\n")

    for i, categoria in enumerate(categorias, start = 1):
        print(f"| [{i}] - {categoria.name}")

    try:
        opcion_categoria = int(input("\nNúmero de categoría: "))
        categoria_elegida = categorias[opcion_categoria - 1]
    except:
        print("\nOpción inválida.")
        input("Presione Enter para volver al menú principal...")
        return

    recetas = list(categoria_elegida.glob("*.txt"))

    if len(recetas) < 1 :
        print("\nAún no hay recetas escritas en esta categoría.")
        input("Presione Enter para volver al menú principal...")
        return  

    print("\nSelecciona una receta:\n")

    for i, receta in enumerate(recetas, start = 1):
        print(f"| [{i}] - {receta.name}")

    try:
        opcion_receta = int(input("\nNúmero de receta: "))
        receta_elegida = recetas[opcion_receta - 1]
    except:
        print("\nOpción inválida.")
        input("Presione Enter para volver al menú principal...")
        return

    print("\n--- CONTENIDO ---\n")
    print(receta_elegida.read_text())

    input("\nPresione Enter para volver al menú principal...")


# 2. Creador de receta
def nueva_receta(base):
    system("cls")

    categorias = [carpeta for carpeta in base.iterdir() if carpeta.is_dir()]

    print("Selecciona una categoría para añadir una receta nueva:\n")

    for i, categoria in enumerate(categorias, start = 1):
        print(f"| [{i}] - {categoria.name}")

    try:
        opciones = int(input("\nNúmero de categoría: "))
        categoria_elegida = categorias[opciones - 1]
    except:
        print("\n¡Error: opción inválida!")
        input("Presione Enter para volver al menú principal...")
        return

    nombre_receta = input("\nIngrese el nombre de la receta que desea añadir: ")

    nueva_ruta = categoria_elegida / f"{nombre_receta}.txt"

    contenido = input("\nEscribe la receta:\n")

    nueva_ruta.write_text(contenido)

    print("\n¡Receta creada con éxito!")
    input("Presione Enter para volver al menú principal...")

# 3. Crear categoría nueva
def nueva_categoria(base) :
    system("cls")

    nombre_categoria = input("Ingrese el nombre de la categoría que desea añadir: ")

    ruta_nueva = base / nombre_categoria

    try :
        ruta_nueva.mkdir()
        print("\n¡Categoría creada con éxito!")
    except :
        print("\n¡Error: esta categoría ya existe!")

    input("Presiones Enter para volver al menú principal...")

# 4. Eliminar receta
def eliminar_receta(base):
    system("cls")

    categorias = [carpeta for carpeta in base.iterdir() if carpeta.is_dir()]

    print("Selecciona una categoría:\n")

    for i, categoria in enumerate(categorias, start = 1):
        print(f"| [{i}] - {categoria.name}")

    try:
        opcion_categoria = int(input("\nNúmero de categoría: "))
        categoria_elegida = categorias[opcion_categoria - 1]
    except:
        print("\nOpción inválida.")
        input("Presione Enter para volver al menú principal...")
        return

    recetas = list(categoria_elegida.glob("*.txt"))

    print("\nSelecciona una receta para eliminar:\n")

    for i, receta in enumerate(recetas, start = 1):
        print(f"| [{i}] - {receta.name}")

    try:
        opcion_receta = int(input("\nNúmero de receta: "))
        receta_elegida = recetas[opcion_receta - 1]
    except:
        print("\nOpción inválida.")
        input("Presione Enter para volver al menú principal...")
        return

    if receta_elegida.exists():
        receta_elegida.unlink()
        print(f"\nEl archivo {receta_elegida.name} ha sido eliminado.")
    else:
        print("\nEl archivo no existe.")

    input("Presione Enter para volver al menú principal...")

# 5. Eliminar categoría
def eliminar_categoria(base) :
    system("cls")

    categorias = [carpeta for carpeta in base.iterdir() if carpeta.is_dir()]

    if not categorias:
        print("Aún no hay categorías creadas.")
        input("Presione Enter para volver al menú principal...")
        return

    print("Selecciona una categoría:\n")

    for i, categoria in enumerate(categorias, start = 1):
        print(f"| [{i}] - {categoria.name}")

    try:
        opcion_categoria = int(input("\nNúmero de categoría: "))
        categoria_elegida = categorias[opcion_categoria - 1]
    except:
        print("\nOpción inválida.")
        input("Presione Enter para volver al menú principal...")
        return

    shutil.rmtree(categoria_elegida)

    print(f'\n¡Categoría "{categoria_elegida.name}" eliminada con éxito!')
    input("Presione Enter para volver al menú principal...")

# ----- Inicio del programa -----

system("cls")

print("¡Saludos Chef!")
input("Presione Enter para comenzar...")

base = Path(__file__).parent / "Recetas"

while True:
    system("cls")

    print(f"Las recetas están en el directorio: {base}")

    cantidad = list(base.rglob("*.txt"))
    print(f"Hay en total {len(cantidad)} archivo(s)\n")

    try:
        n = int(input(
            "Ingrese una de las siguientes opciones:\n"
            "| [1] - Leer receta\n"
            "| [2] - Crear receta\n"
            "| [3] - Crear categoría\n"
            "| [4] - Eliminar receta\n"
            "| [5] - Eliminar categoría\n"
            "| [6] - Finalizar lector de recetas\n"
            "Por favor, ingresa una opción: "
        ))
    except ValueError:
        print("\n¡Error! Debes ingresar un número.")
        input("Presione Enter para continuar...")
        continue

    if n == 6:
        break
    elif n < 1 or n > 6:
        print("\n¡Error: ingrese una opción válida!")
        input("Presione Enter para continuar...")
        continue

    if n == 1:
        leer_receta(base)
    elif n == 2:
        nueva_receta(base)
    elif n == 3:
        nueva_categoria(base)
    elif n == 4:
        eliminar_receta(base)
    elif n == 5:
        eliminar_categoria(base)

# ----- Fin del programa -----

system("cls")

print("¡Programa finalizado, vuelva pronto!")
