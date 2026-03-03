"""
Author: Braulinho
Description: Console application to manage recipes by categories.
"""

# ----- Libraries -----

from pathlib import Path
from os import system
import shutil

# ----- Functions -----

# 1. Read recipe
def read_recipe(base):
    system("cls")

    categories = [folder for folder in base.iterdir() if folder.is_dir()]

    print("Select a category:\n")

    for i, category in enumerate(categories, start=1):
        print(f"| [{i}] - {category.name}")

    try:
        category_option = int(input("\nCategory number: "))
        chosen_category = categories[category_option - 1]
    except:
        print("\nInvalid option.")
        input("Press Enter to return to the main menu...")
        return

    recipes = list(chosen_category.glob("*.txt"))

    if len(recipes) < 1:
        print("\nThere are no recipes in this category yet.")
        input("Press Enter to return to the main menu...")
        return

    print("\nSelect a recipe:\n")

    for i, recipe in enumerate(recipes, start=1):
        print(f"| [{i}] - {recipe.name}")

    try:
        recipe_option = int(input("\nRecipe number: "))
        chosen_recipe = recipes[recipe_option - 1]
    except:
        print("\nInvalid option.")
        input("Press Enter to return to the main menu...")
        return

    print("\n--- CONTENT ---\n")
    print(chosen_recipe.read_text())

    input("\nPress Enter to return to the main menu...")

# 2. Create recipe
def new_recipe(base):
    system("cls")

    categories = [folder for folder in base.iterdir() if folder.is_dir()]

    print("Select a category to add a new recipe:\n")

    for i, category in enumerate(categories, start=1):
        print(f"| [{i}] - {category.name}")

    try:
        option = int(input("\nCategory number: "))
        chosen_category = categories[option - 1]
    except:
        print("\nError: invalid option!")
        input("Press Enter to return to the main menu...")
        return

    recipe_name = input("\nEnter the name of the recipe you want to add: ")

    new_path = chosen_category / f"{recipe_name}.txt"

    content = input("\nWrite the recipe:\n")

    new_path.write_text(content)

    print("\nRecipe created successfully!")
    input("Press Enter to return to the main menu...")

# 3. Create new category
def new_category(base):
    system("cls")

    category_name = input("Enter the name of the category you want to add: ")

    new_path = base / category_name

    try:
        new_path.mkdir()
        print("\nCategory created successfully!")
    except:
        print("\nError: this category already exists!")

    input("Press Enter to return to the main menu...")

# 4. Delete recipe
def delete_recipe(base):
    system("cls")

    categories = [folder for folder in base.iterdir() if folder.is_dir()]

    print("Select a category:\n")

    for i, category in enumerate(categories, start=1):
        print(f"| [{i}] - {category.name}")

    try:
        category_option = int(input("\nCategory number: "))
        chosen_category = categories[category_option - 1]
    except:
        print("\nInvalid option.")
        input("Press Enter to return to the main menu...")
        return

    recipes = list(chosen_category.glob("*.txt"))

    if not recipes:
        print("\nThere are no recipes in this category.")
        input("Press Enter to return to the main menu...")
        return

    print("\nSelect a recipe to delete:\n")

    for i, recipe in enumerate(recipes, start=1):
        print(f"| [{i}] - {recipe.name}")

    try:
        recipe_option = int(input("\nRecipe number: "))
        chosen_recipe = recipes[recipe_option - 1]
    except:
        print("\nInvalid option.")
        input("Press Enter to return to the main menu...")
        return

    if chosen_recipe.exists():
        chosen_recipe.unlink()
        print(f"\nFile {chosen_recipe.name} has been deleted.")
    else:
        print("\nFile does not exist.")

    input("Press Enter to return to the main menu...")

# 5. Delete category
def delete_category(base):
    system("cls")

    categories = [folder for folder in base.iterdir() if folder.is_dir()]

    if not categories:
        print("There are no categories created yet.")
        input("Press Enter to return to the main menu...")
        return

    print("Select a category:\n")

    for i, category in enumerate(categories, start=1):
        print(f"| [{i}] - {category.name}")

    try:
        category_option = int(input("\nCategory number: "))
        chosen_category = categories[category_option - 1]
    except:
        print("\nInvalid option.")
        input("Press Enter to return to the main menu...")
        return

    shutil.rmtree(chosen_category)

    print(f'\nCategory "{chosen_category.name}" deleted successfully!')
    input("Press Enter to return to the main menu...")

# ----- Program Start -----

system("cls")

print("Greetings, Chef!")
input("Press Enter to begin...")

base = Path(__file__).parent / "Recetas"
base.mkdir(exist_ok = True)

while True:
    system("cls")

    print(f"Recipes are located in: {base}")

    total_files = list(base.rglob("*.txt"))
    print(f"There are {len(total_files)} file(s) in total.\n")

    try:
        n = int(input(
            "Choose one of the following options:\n"
            "| [1] - Read recipe\n"
            "| [2] - Create recipe\n"
            "| [3] - Create category\n"
            "| [4] - Delete recipe\n"
            "| [5] - Delete category\n"
            "| [6] - Exit recipe manager\n"
            "Please enter an option: "
        ))
    except ValueError:
        print("\nError! You must enter a number.")
        input("Press Enter to continue...")
        continue

    if n == 6:
        break
    elif n < 1 or n > 6:
        print("\nError: please enter a valid option!")
        input("Press Enter to continue...")
        continue

    if n == 1:
        read_recipe(base)
    elif n == 2:
        new_recipe(base)
    elif n == 3:
        new_category(base)
    elif n == 4:
        delete_recipe(base)
    elif n == 5:
        delete_category(base)

# ----- End of Program -----

system("cls")
print("Program finished. Come back soon!")
