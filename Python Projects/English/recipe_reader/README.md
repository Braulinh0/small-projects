# 🍳 Recipe Reader in Python

Small console application that allows you to:

- 📖 Read recipes  
- ➕ Create recipes  
- 📂 Create categories  
- ❌ Delete recipes  
- 🗑️ Delete categories  

## 🛠 Technologies Used
- Python  
- Standard libraries: `pathlib`, `os`, `shutil`

## ▶ How to Run

1. Clone the repository  
2. Run:

```
python main.py
```

## 📁 Structure

Recipes are stored inside the `Recetas/` folder.  
Each category is a folder.  
Each recipe is a `.txt` file.

## 🚨 Recommendations

1. If you are going to add a recipe, avoid using strings that include the character `ñ` or accent marks.
- Example of encoding error:
```
azÃºcar / BaÃ±a
```

---

<p align="center">
  Project created by Braulinho 😏
</p>
